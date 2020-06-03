version_to_brave_core_milestone_ids = {
    '1.1.x': 34,
    '1.2.x': 39,
    '1.3.x': 41,
    '1.4.x': 44,
    '1.5.x': 48,
    '1.6.x': 0,  # Was never released, merged to 1.7.x
    '1.7.x': 55,
    '1.8.x': 58,
    '1.9.x': 63,
    '1.10.x': 66,
    '1.11.x': 72,
}

version_to_brave_browser_milestone_ids = {
    '1.1.x': 50,
    '1.2.x': 57,
    '1.3.x': 62,
    '1.4.x': 65,
    '1.5.x': 72,
    '1.6.x': 0,  # Was never released, merged to 1.7.x
    '1.7.x': 84,
    '1.8.x': 92,
    '1.9.x': 98,
    '1.10.x': 104,
    '1.11.x': 112,
}

closed_labels = set([
    'closed/invalid',
    'closed/not-actionable',
    'closed/fixed-by-component-update',
    'closed/works-for-me',
    'closed/no-milestone',
    'duplicate',
    'wontfix',
    'question',
    'support',
    'stale',
])

qa_labels = set([
    'QA/Yes',
    'QA/No',
])

release_note_labels = set([
    'release-notes/include',
    'release-notes/exclude',
])

github_slack_map = {
    'alexandersjosten': '@asjosten',
    'AlexeyBarabash': '@alexey',
    'AndriusA': '@Andrius',
    'antonok-edm': '@alazarev',
    'bbondy': '@bbondy',
    'brave-builds': '#build-bot',
    'bridiver': '@bjohnson',
    'Brandon-T': '@bthomas',
    'bsclifton': '@clifton',
    'cezaraugusto': '@clifton',
    'darkdh': '@anthony',
    'deeppandya': '@dpandya',
    'diracdeltas': '@yan',
    'emerick': '@erogul',
    'fmarier': '@francois',
    'gdregalo': '@nejczdovc',
    'Genysys': '@sdare',
    'gpestana': '@gpestana',
    'iccub': '@mbuczek',
    'iefremov': '@iefremov',
    'jamesmudgett': '@james',
    'jumde': '@pranjal',
    'keur': '@keur',
    'kjozwiak': '@kamil',
    'kylehickinson': '@khickinson',
    'LaurenWags': '@lauren',
    'linhkikuchi': '@linhn',
    'mbacchi': '@mbacchi',
    'mihaiplesa': '@mplesa',
    'mkarolin': '@mkarolinskiy',
    'moritzhaller': '@mhaller',
    'NejcZdovc': '@nejczdovc',
    'petemill': '@petemill',
    'pilgrim-brave': '@mpilgrim',
    'ryanml': '@rlanese',
    'samartnik': '@artem',
    'SergeyZhukovsky': '@serg',
    'simonhong': '@shong',
    'srirambv': '@sriram',
    'tomlowenthal': '@yan',
    'tmancey': '@tmancey',
    'yrliou': '@yrliou',
    'zenparsing': '@ksmith',
}


branch_regex = r'^1\.[1-9]\d*\.x+$'

brave_core_milestone_ids_to_version = {v: k for k, v in version_to_brave_core_milestone_ids.items()}
brave_browser_milestone_ids_to_version = {v: k for k, v in version_to_brave_browser_milestone_ids.items()}
