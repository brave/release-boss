version_to_brave_core_milestone_ids = {
    '1.1.x': 34,
    '1.2.x': 39,
    '1.3.x': 41,
    '1.4.x': 44,
    '1.5.x': 48,
    '1.6.x': 0,  # Was never released, merged to 1.7.x
    '1.7.x': 55,
    '1.8.x': 58, '1.9.x': 63,
    '1.10.x': 66,
    '1.11.x': 72,
    '1.12.x': 74,
    '1.13.x': 83,
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
    '1.12.x': 115,
    '1.13.x': 126,
}

closed_labels = set([
    'closed/invalid',
    'closed/not-actionable',
    'closed/fixed-by-component-update',
    'closed/works-for-me',
    'closed/no-milestone',
    'closed/stale',
    'closed/wontfix',
    'closed/duplicate',
    'closed/by-author',
    'question',
    'support'
])

qa_labels = set([
    'QA/Yes',
    'QA/No',
])

release_note_labels = set([
    'release-notes/include',
    'release-notes/exclude',
])

os_labels = set([
    'OS/macOS',
    'OS/Windows',
    'OS/Linux',
    'OS/Android',
    'OS/Desktop',
    'OS/iOS',
])

github_slack_map = {
    'AlanBreck ':'UTS3SMFB2',
    'AlexeyBarabash': 'U70RB43BP',
    'AndriusA': 'UC1CMB9D5',
    'antonok-edm': 'UL1L3CH61',
    'anthonypkeane': 'UCLMABWMS',
    'bbondy': 'U04PX1BUA',
    'bridiver': 'U0D101U31',
    'Brandon-T': 'UK6RSD8ET',
    'Brave-Matt': 'UB9GJLKDY',
    'bsclifton': 'U13AH4AJY',
    'btlechowski': 'U8M8YQNRJ',
    'cezaraugusto': 'U13AH4AJY',
    'darkdh': 'U1M7ELUSV',
    'deeppandya': 'UK2T5MQRM',
    'diracdeltas': 'U0B9C844X',
    'emerick': 'U9E5WAX34',
    'fmarier': 'UFAJB5HB8',
    'Fanboynz': 'UK7MJJX44',
    'gdregalo': 'U3MLL9K8C',
    'GeetaSarvadnya': 'UAA2QRP17',
    'Genysys': 'ULC9D16TH',
    'goodov': 'U01N082FZ0S',
    'gpestana': 'UK1C3AZMJ',
    'Gyuyoung': 'U0170E17UQL',
    'iccub': 'U815AK5JS',
    'iefremov': 'UE87NRK2A',
    'jamesmudgett': 'U2APFJL5P',
    'jonathansampson': 'U2D8DG0EM',
    'jsecretan': 'U08PTRJT1',
    'jumde': 'U68S7NAFK',
    'justnom': 'U01AS121HUH',
    'karenkliu': 'UB9B8D46Q',
    'keur': 'UK776151S',
    'kjozwiak': 'U3MRXKK1Q',
    'kylehickinson': 'UAR38EQTG',
    'LaurenWags': 'U5HCYJGUV',
    'linhkikuchi': 'UKNGLUHC6',
    'mariospr': 'U0170E1A3GC',
    'marshall': 'U04PX1BUA',
    'mbacchi': 'UBU5ZJ5NC',
    'mherrmann': 'U01124T2AHG',
    'mihaiplesa': 'UBU5ZJ5NC',
    'mkarolin': 'UC4RZJMSB',
    'moritzhaller': 'UM5GQEGBV',
    'mrobinson': 'U0170E1AXRS',
    'NejcZdovc': 'U3MLL9K8C',
    'orspetol': 'U01GPJW3QKE',
    'pes10k': 'U5H3AC7LL',
    'petemill': 'U7CQA0TST',
    'pilgrim-brave': 'UD4490KT4',
    'rebron': 'UBYNQGBUG',
    'ryanbr': 'UK7MJJX44',
    'ryanml': 'U04PX1BUA',
    'samartnik': 'U6GV4FVD4',
    'SergeyZhukovsky': 'U0D73ULKD',
    'simonhong': 'U9V31L3L0',
    'soner-yuksel': 'U01DVT6HXBR',
    'spylogsster': 'U01LH63CLTD',
    'srirambv': 'U1U85R2ES',
    'stephendonner': 'U01JEJCV4N7',
    'tomlowenthal': 'U0B9C844X',
    'tmancey': 'UB9PF4X5K',
    'wchen342': 'U01PRHY091A',
    'wknapik': 'U01PAAE67FZ',
    'yachtcaptain23': 'UAFGJQ602',
    'yrliou': 'U88QJKZBP',
    'zenparsing': 'UU7NY6Q9L',
}


branch_regex = r'^1\.[1-9]\d*\.x+$'

brave_core_milestone_ids_to_version = {v: k for k, v in version_to_brave_core_milestone_ids.items()}
brave_browser_milestone_ids_to_version = {v: k for k, v in version_to_brave_browser_milestone_ids.items()}
slack_github_map = {v: k for k, v in github_slack_map.items()}
