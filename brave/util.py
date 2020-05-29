from collections import Counter
from github import Github
import re
import datetime
from . import config
import time


def rate_limit_for_value(g, val):
    (avail, total) = g.rate_limiting
    print('Rate limiting info - total:', total, 'avail: ', avail)

    reset_time = datetime.datetime.fromtimestamp(g.rate_limiting_resettime)
    delay_seconds = (reset_time - datetime.datetime.now()).total_seconds()

    if avail < 50:
        print('Less than 50 rate limited requests left, delaying for', delay_seconds, 'seconds...')
        # Wait an extra 10 seconds to be safe
        time.sleep(delay_seconds + 10)
        print('Resumed.')

    return val


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

    pull_refs_master = [config.milestone_ids_to_version[x.milestone.number] for x in pulls if
                        rate_limit_for_value(g, x.base.ref) == 'master' and
                        x.milestone is not None and
                        x.milestone.number in config.milestone_ids_to_version.keys() and
                        bool(re.match(config.branch_regex, config.milestone_ids_to_version[x.milestone.number]))]
    pull_refs_uplift = [x.base.ref for x in pulls if
                        rate_limit_for_value(g, bool(re.match(config.branch_regex, x.base.ref))) and
                        x.milestone is not None and
                        config.version_to_milestone_ids[x.base.ref] == x.milestone.number]
    print('master:', Counter(pull_refs_master).most_common(100).sort(key=sort_branch_count_pairs))
    print('uplifts: ', Counter(pull_refs_uplift).most_common(100).sort(key=sort_branch_count_pairs))
    return (pull_refs_master, pull_refs_uplift)


def recent_prs_with_no_milestones(github_access_token, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    g = Github(github_access_token)
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    pulls = repo.get_pulls('closed')

    today = datetime.datetime.now()
    past_date = today - datetime.timedelta(days=30)

    pulls = [x.html_url for x in pulls if
             rate_limit_for_value(g, x.merged_at) is not None and
             x.merged_at > past_date and
             x.milestone is None]
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
              not bool(config.closed_labels.intersection([y.name for y in x.labels]))]
    print('issues: ', issues)
    return issues
