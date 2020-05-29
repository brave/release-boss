from collections import Counter
from github import Github
import re
import datetime
from . import config


def sort_branch_count_pairs(branch_val):
    (branch, val) = branch_val
    if branch == 'master':
        return 1
    parts = branch.split('.')
    val = int(parts[0]) * 1000 + int(parts[1])
    return val


def get_pull_requests(g, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    pulls = repo.get_pulls('closed')

    pull_refs_master = [config.milestone_ids_to_version[x.milestone.number] for x in pulls if
                        x.base.ref == 'master' and
                        x.milestone is not None and
                        x.milestone.number in config.milestone_ids_to_version.keys() and
                        bool(re.match(config.branch_regex, config.milestone_ids_to_version[x.milestone.number]))]
    pull_refs_uplift = [x.base.ref for x in pulls if
                        bool(re.match(config.branch_regex, x.base.ref)) and
                        x.milestone is not None and
                        config.version_to_milestone_ids[x.base.ref] == x.milestone.number]
    print('master:', Counter(pull_refs_master).most_common(100).sort(key=sort_branch_count_pairs))
    print('uplifts: ', Counter(pull_refs_uplift).most_common(100).sort(key=sort_branch_count_pairs))
    return (pull_refs_master, pull_refs_uplift)


def recent_prs_with_no_milestones(g, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    pulls = repo.get_pulls('closed')

    today = datetime.datetime.now()
    past_date = today - datetime.timedelta(days=30)

    pulls = [x.html_url for x in pulls if
             x.milestone is None and
             x.merged_at is not None and
             x.merged_at > past_date]
    print('pulls: ', pulls)
    return pulls


def recent_issues_with_no_milestones(g, repo_stub):
    [org_name, repo_name] = repo_stub.split("/")
    org = g.get_organization(org_name)
    repo = org.get_repo(repo_name)
    issues = repo.get_issues(state="closed")

    today = datetime.datetime.now()
    past_date = today - datetime.timedelta(days=30)

    issues = [(x.html_url, x.labels)
              for x in issues
              if x.pull_request is None
              and x.milestone is None
              and x.closed_at is not None
              and x.closed_at > past_date
              and bool(config.closed_labels.intersection([y.name for y in x.labels]))]
    print('issues: ', issues)
    return issues
