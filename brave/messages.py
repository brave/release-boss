def missing_qa_flags(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s (%s) closed issue %s without the needed QA flags.

Please specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.

Thank you!
    ''' % (closed_by_login, closed_by_name, html_url)).strip()
