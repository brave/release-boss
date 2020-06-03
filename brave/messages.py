def missing_qa_flags(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s (%s) closed issue %s without the needed QA flags.

Please specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.

Thank you!
    ''' % (closed_by_login, closed_by_name, html_url)).strip()


def missing_release_note_flags(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s (%s) closed issue %s without the needed release note flags.

Please specify either `release-notes/include` or `release-notes/exclude`.
If you specify `release-notes/include`, then please ensure the title of the issue is appropriate for release notes.

Thank you!
    ''' % (closed_by_login, closed_by_name, html_url)).strip()
