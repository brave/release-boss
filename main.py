import argparse
import datetime
import os
import re
from brave import config, util
from collections import Counter
from github import Github


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--action', help='''One of:
        pr-per-release: Output data for the number of PRs per release
        pr-milestone: Output data for the PRs that are missing milestones''')
    args = parser.parse_args()

    assert "GITHUB_ACCESS_TOKEN" in os.environ, "Access token must be specified with GITHUB_ACCESS_TOKEN"
    access_token = os.environ['GITHUB_ACCESS_TOKEN']
    g = Github(access_token)

    if args.action == 'pr-per-release':
        util.get_pull_requests(g, "brave/brave-core")
    elif args.action == 'pr-milestone':
        util.recent_prs_with_no_milestones(g, "brave/brave-core")
    else:
        print('Not a valid command: ', args.action)


if __name__ == "__main__":
    main()
