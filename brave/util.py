from collections import Counter
from github import Github
import re
import datetime
from . import config, messages, parsing, slack
import time


def rate_limit_for_value(g, val=None):
    (avail, total) = g.rate_limiting
    # print('Rate limiting info - total:', total, 'avail: ', avail)

    reset_time = datetime.datetime.fromtimestamp(g.rate_limiting_resettime)
    delay_seconds = (reset_time - datetime.datetime.now()).total_seconds()

    if avail < 50:
        print('Less than 50 rate limited requests left, delaying for', delay_seconds, 'seconds...')
        # Wait an extra 10 seconds to be safe
        time.sleep(delay_seconds + 10)
        print('Resumed.')

    return val


def item_has_no_label_intersection(item, labels):
    return not bool(labels.intersection([y.name for y in item.labels]))


def sort_branch_count_pairs(branch_val):
    (branch, val) = branch_val
    if branch == 'master':
        return 1
    parts = branch.split('.')
    val = int(parts[0]) * 1000 + int(parts[1])
    return val


def get_pull_requests(github_access_token, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    g = Github(github_access_token)
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    pulls = repo.get_pulls('closed')

    pull_refs_master = [config.brave_core_milestone_ids_to_version[x.milestone.number] for x in pulls if
                        rate_limit_for_value(g, x.base.ref) == 'master' and
                        x.milestone is not None and
                        x.milestone.number in config.brave_core_milestone_ids_to_version.keys() and
                        bool(re.match(config.branch_regex, config.brave_core_milestone_ids_to_version[x.milestone.number]))]
    pull_refs_uplift = [x.base.ref for x in pulls if
                        rate_limit_for_value(g, bool(re.match(config.branch_regex, x.base.ref))) and
                        x.milestone is not None and
                        config.version_to_brave_core_milestone_ids[x.base.ref] == x.milestone.number]

    master = Counter(pull_refs_master).most_common(100)
    master.sort(key=sort_branch_count_pairs)

    uplifts = Counter(pull_refs_uplift).most_common(100)
    uplifts.sort(key=sort_branch_count_pairs)

    print('uplifts: ', uplifts)
    print('master:', master)
    return (master, uplifts)


def recent_prs_with_no_milestones(github_access_token, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    g = Github(github_access_token)
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    pulls = repo.get_pulls('closed')

    today = datetime.datetime.now()
    past_date = today - datetime.timedelta(days=120)

    pulls = [x.html_url for x in pulls if
             rate_limit_for_value(g, x.merged_at) is not None and
             x.merged_at > past_date and
             x.milestone is None and
             # Ignore PRs that were merged into other PRs
             x.base.ref == 'master' and
             x.title != 'Branch migration - master branch']
    print('pulls: ', pulls)
    return pulls


def recent_issues_with_no_milestones(github_access_token, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    g = Github(github_access_token)
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    issues = repo.get_issues(state="closed")

    today = datetime.datetime.now()
    past_date = today - datetime.timedelta(days=30)

    issues = [x.html_url for x in issues if
              rate_limit_for_value(g, x.closed_at) is not None and
              x.closed_at > past_date and
              x.pull_request is None and
              x.milestone is None and
              item_has_no_label_intersection(x, config.closed_labels)]
    print('issues: ', issues)
    return issues


def fix_milestone_pr(g, pull, pr_repo_stub):
    match = parsing.get_closed_issue(pull.body, pr_repo_stub)
    if not match:
        # print('Match not found pr.number:', pull.number)
        return

    (closed_repo_stub, closed_number) = match
    if len(closed_repo_stub.split("/")) == 1:
        print('There is a problem with this pull body: ', pull.body)
        print('There is a problem with this pull number: ', pull.number)
        return

    if closed_repo_stub != 'brave/brave-browser':
        # print('Skipping because repo: ', closed_repo_stub, 'for PR number: ', pull.number)
        return

    [closed_org_name, closed_repo_name] = closed_repo_stub.split("/")
    org = g.get_organization(closed_org_name)
    # print('closed_number: ', closed_number)
    # print('closed_org_name: ', closed_org_name)
    # print('closed_repo_name: ', closed_repo_name)
    repo = org.get_repo(closed_repo_name)
    issue = repo.get_issue(closed_number)

    # If the issue already has a milestone, don't override it
    if issue.milestone is not None:
        return None

    # Make sure the issue is closed
    if issue.closed_at is None:
        return None

    # If the issue has an invalid-like label, then don't consider it
    if bool(config.closed_labels.intersection([y.name for y in issue.labels])):
        return None

    return issue.html_url


def fix_milestone_prs(github_access_token, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    g = Github(github_access_token)
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    pulls = repo.get_pulls('closed')

    today = datetime.datetime.now()
    # past_date = today - datetime.timedelta(days=160)
    pull_refs_master = [x for x in pulls if
                        rate_limit_for_value(g, x.closed_at) is not None and
                        # x.closed_at > past_date and
                        rate_limit_for_value(g, x.base.ref) == 'master' and
                        x.milestone is not None]
    for pull in pull_refs_master:
        rate_limit_for_value(g)
        issue_url = fix_milestone_pr(g, pull, repo_stub)
        if issue_url is not None:
            print(issue_url,
                  pull.milestone.number,
                  config.brave_core_milestone_ids_to_version[pull.milestone.number] if
                  pull.milestone.number in config.brave_core_milestone_ids_to_version else
                  '')


def fix_missing_qa_flags(slack_access_token, github_access_token, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    g = Github(github_access_token)
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    milestone = repo.get_milestone(config.version_to_brave_browser_milestone_ids['1.10.x'])
    issues = repo.get_issues(state="closed", milestone=milestone)
    items_to_notify = [(x.html_url, x.closed_by.login, x.closed_by.name) for x in issues if
            x.pull_request is None and
            item_has_no_label_intersection(x, config.qa_labels)]
    if bool(slack_access_token):
        for i in items_to_notify:
            (html_url, closed_by_login, closed_by_name) = i
            slack_id_to_notify = config.github_slack_map[closed_by_login]
            if bool(slack_id_to_notify):
                slack.notify_user(slack_access_token, slack_id_to_notify,
                        messages.missing_qa_flags(closed_by_login, closed_by_name, html_url))
    print('urls without QA flags', items_to_notify)
