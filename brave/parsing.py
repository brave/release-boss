import re
from urllib.parse import urlparse


def get_closed_issue(body, default_repo_stub):
    p = re.compile('\\b(close|closes|closed|fix|fixes|fixed|resolve|resolves|resolved)\\b(.+)\\b', re.IGNORECASE)
    m = p.search(body)
    if not m:
        print('no match')
        return None
    closed_issue = m.group(2).strip()

    closed_repo_stub = None
    closed_number = None

    # Check if we have something like Fix brave/brave-core#3131
    simple_syntax_split = closed_issue.split('#')
    if len(simple_syntax_split) == 2:
        (closed_repo_stub, closed_number) = closed_issue.split('#')
        closed_repo_stub = closed_repo_stub if bool(closed_repo_stub) else default_repo_stub

    # Check if we have something like Fix https://github.com/brave/brave-core/issues/3131
    url_path_split = urlparse(closed_issue).path.split('/')
    if len(url_path_split) == 5:
        closed_repo_stub = url_path_split[1] + '/' + url_path_split[2]
        closed_number = url_path_split[4]
    if not bool(closed_repo_stub):
        print('closed repo stub is not valid:', body)
        return None
    if not bool(closed_number):
        print('closed number is not valid:', body)
        return None
    return (closed_repo_stub, closed_number.split()[0])
