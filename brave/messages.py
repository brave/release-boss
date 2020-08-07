def format_name(closed_by_login, closed_by_name):
    if closed_by_name:
        return '%s (%s)' % (closed_by_login, closed_by_name)
    return closed_by_login


def missing_os_and_qa_and_rel_note_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed OS, QA, and release note labels.

Please specify at least one of `OS/macOS`, `OS/Windows`, `OS/Linux`, `OS/Android`, `OS/Desktop` or `OS/iOS`.
For more information see https://github.com/brave/brave-browser/wiki/Missing-OS-labels

Please also specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.

Please also specify either `release-notes/include` or `release-notes/exclude`.

For more information see:
- https://github.com/brave/brave-browser/wiki/Missing-OS-labels
- https://github.com/brave/brave-browser/wiki/Missing-release-note-labels
- https://github.com/brave/brave-browser/wiki/Missing-QA-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_os_and_qa_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed OS and QA labels.

Please specify at least one of `OS/macOS`, `OS/Windows`, `OS/Linux`, `OS/Android`, `OS/Desktop`, or `OS/iOS`.

Please specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.

For more information see https://github.com/brave/brave-browser/wiki/Missing-OS-labels and
https://github.com/brave/brave-browser/wiki/Missing-QA-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_os_and_rel_note_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed OS and release note labels.

Please specify at least one of `OS/macOS`, `OS/Windows`, `OS/Linux`, `OS/Android`, `OS/Desktop` or `OS/iOS`.

Please also specify either `release-notes/include` or `release-notes/exclude`.

For more information see https://github.com/brave/brave-browser/wiki/Missing-OS-labels and
https://github.com/brave/brave-browser/wiki/Missing-release-note-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_qa_and_rel_note_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed QA and release note labels.

Please specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.

Please also specify either `release-notes/include` or `release-notes/exclude`.
For more information see https://github.com/brave/brave-browser/wiki/Missing-release-note-labels and
https://github.com/brave/brave-browser/wiki/Missing-QA-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_qa_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed QA labels.

Please specify either `QA/Yes` or `QA/No`.
If you specify `QA/Yes`, then please also specify a test plan.
For more information see https://github.com/brave/brave-browser/wiki/Missing-QA-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_release_note_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed release note labels.

Please specify either `release-notes/include` or `release-notes/exclude`.
For more information see https://github.com/brave/brave-browser/wiki/Missing-release-note-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_os_labels(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without the needed OS labels.

Please specify at least one of `OS/macOS`, `OS/Windows`, `OS/Linux`, `OS/Android`, `OS/Desktop`, or `OS/iOS`.
For more information see https://github.com/brave/brave-browser/wiki/Missing-OS-labels

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_pr_milestone(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed pull request %s without specifying a milestone.

Please update the milestone to match the version it landed in.
For more information see https://github.com/brave/brave-browser/wiki/Pull-requests-with-missing-milestones

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()


def missing_issue_milestone(closed_by_login, closed_by_name, html_url):
    return (r'''
Github user %s closed issue %s without specifying a milestone.

Please update the milestone to match the version it landed in.
For more information see https://github.com/brave/brave-browser/wiki/Issue-with-missing-milestones

Thank you!
    ''' % (format_name(closed_by_login, closed_by_name), html_url)).strip()
