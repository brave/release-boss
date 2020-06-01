from . import parsing


def test_get_closed_issue():
    data = 'Fix #3131\nxxxxx'
    assert parsing.get_closed_issue(data, 'brave/brave-browser') == ('brave/brave-browser', '3131')

    data = ' Closes brave/brave-core#3132\nxxxxx fdsaf sad fasd fdsa '
    assert parsing.get_closed_issue(data, 'brave/brave-browser') == ('brave/brave-core', '3132')

    data = 'a CloseS brave/brave-core#3133\nxxxxx fdsaf sad fasd fdsa '
    assert parsing.get_closed_issue(data, 'brave/brave-core') == ('brave/brave-core', '3133')

    data = 'Fix https://github.com/brave/brave-core/issues/3134'
    assert parsing.get_closed_issue(data, 'brave/brave-core') == ('brave/brave-core', '3134')

    data = 'a Closes https://www.github.com/brave/brave-core/issues/3135 dsa\nxxxxx fdsaf sad fasd fdsa '
    assert parsing.get_closed_issue(data, 'brave/brave-core') == ('brave/brave-core', '3135')

    data = 'a Closes https://www.github.com/brave/brave-core/issues/3136 dsa\nxxxxx fdsaf sad fasd fdsa '
    assert parsing.get_closed_issue(data, 'brave/brave-core') == ('brave/brave-core', '3136')

    data = '''
    fdasfdsaa FiXeD https://www.github.com/brave/brave-core/issues/3136 dsa\nxxxxx fdsaf sad fasd fdsa
    '''
    assert parsing.get_closed_issue(data, 'brave/brave-core') == ('brave/brave-core', '3136')
