import argparse
import os
from brave import config, slack, util


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--action', help='''One of:
        pr-per-release: Output data for the number of PRs per release
        pr-milestone: Output data for the PRs that are missing milestones
        issue-milestone: Output data for the issues that are missing milestones
        fix-milestone-prs: Output data for issues that have no milestone, but associated PR does
        fix-missing-issue-labels: Sends at most 1 message per issue that needs any combination of labels''')
    args = parser.parse_args()

    assert 'GITHUB_ACCESS_TOKEN' in os.environ, 'Access token must be specified with GITHUB_ACCESS_TOKEN'

    github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
    slack_notify = False if 'SLACK_NOTIFY' in os.environ and os.environ['SLACK_NOTIFY'] == 'no' else True
    slack_access_token = os.environ['SLACK_ACCESS_TOKEN'] if 'SLACK_ACCESS_TOKEN' in os.environ and slack_notify else ''

    if not slack_access_token and slack_notify:
        print('Warning: Slack token not specified, so no Slack notifications will be given')

    if args.action == 'pr-per-release':
        util.get_pull_requests(github_access_token, 'brave/brave-core')
    elif args.action == 'fix-milestone-prs':
        util.fix_milestone_prs(github_access_token, 'brave/brave-core')
    elif args.action == 'fix-missing-issue-labels':
        util.fix_missing_issue_labels(slack_access_token, github_access_token, 'brave/brave-browser')
        util.fix_missing_issue_labels(slack_access_token, github_access_token, 'brave/brave-ios')
    else:
        print('Not a valid command: ', args.action)


if __name__ == '__main__':
    main()
