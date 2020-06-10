def format_name(closed_by_login, closed_by_name):
    if closed_by_name:
        return '%s (%s)' % (closed_by_login, closed_by_name)
    return closed_by_login


def missing_qa_flags(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed QA flags.

Please specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_release_note_flags(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed release note flags.

Please specify either `release-notes/include` or `release-notes/exclude`.
For more information see https://github.com/brave/brave-browser/wiki/Release-notes

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()
