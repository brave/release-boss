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
        fix-missing-qa-flags: Outputs data for issues that are missing QA flags
        fix-missing-release-note-flags: Outputs data for issues that are missing release note flags''')
    args = parser.parse_args()

    assert "GITHUB_ACCESS_TOKEN" in os.environ, "Access token must be specified with GITHUB_ACCESS_TOKEN"

    github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
    slack_access_token = os.environ['SLACK_ACCESS_TOKEN'] if 'SLACK_ACCESS_TOKEN' in os.environ else ''

    if not slack_access_token:
        print('Warning: SLACK_ACCESS_TOKEN not specified, so no Slack notifications will be given')

    if args.action == 'pr-per-release':
        util.get_pull_requests(github_access_token, "brave/brave-core")
    elif args.action == 'pr-milestone':
        util.recent_prs_with_no_milestones(github_access_token, "brave/brave-core")
    elif args.action == 'issue-milestone':
        util.recent_issues_with_no_milestones(github_access_token, "brave/brave-browser")
    elif args.action == 'fix-milestone-prs':
        util.fix_milestone_prs(github_access_token, "brave/brave-core")
    elif args.action == 'fix-missing-qa-flags':
        util.fix_missing_qa_flags(slack_access_token, github_access_token, "brave/brave-browser")
    elif args.action == 'fix-missing-release-note-flags':
        util.fix_missing_release_note_flags(slack_access_token, github_access_token, "brave/brave-browser")
    else:
        print('Not a valid command: ', args.action)


if __name__ == "__main__":
    main()
