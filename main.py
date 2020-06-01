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
        ''')
    args = parser.parse_args()

    assert "GITHUB_ACCESS_TOKEN" in os.environ, "Access token must be specified with GITHUB_ACCESS_TOKEN"
    assert "SLACK_ACCESS_TOKEN" in os.environ, "Access token must be specified with SLACK_ACCESS_TOKEN"

    github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
    slack_access_token = os.environ['SLACK_ACCESS_TOKEN']

    # slack.notify(slack_access_token, '@bbondy', 'Test!')

    if args.action == 'pr-per-release':
        util.get_pull_requests(github_access_token, "brave/brave-core")
    elif args.action == 'pr-milestone':
        util.recent_prs_with_no_milestones(github_access_token, "brave/brave-core")
    elif args.action == 'issue-milestone':
        util.recent_issues_with_no_milestones(github_access_token, "brave/brave-browser")
    elif args.action == 'fix-milestone-prs':
        util.fix_milestone_prs(github_access_token, "brave/brave-core")
    else:
        print('Not a valid command: ', args.action)


if __name__ == "__main__":
    main()
