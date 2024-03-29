import json
import os


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
    'AlanBreck ': 'UTS3SMFB2',
    'AlexeyBarabash': 'U70RB43BP',
    'alexsafe': 'U01Q8K065HU',
    'amirsaber': 'U9JDLSHTN',
    'AndriusA': 'UC1CMB9D5',
    'antonok-edm': 'UL1L3CH61',
    'anthonypkeane': 'UCLMABWMS',
    'arthuredelstein': 'U03CANLQQCA',
    'aseren': 'U026QSEPSHF',
    'atuchin-m': 'U02DG0ATML3',
    'bbondy': 'U04PX1BUA',
    'boocmp': 'U037VLBGZV0',
    'bridiver': 'U0D101U31',
    'Brandon-T': 'UK6RSD8ET',
    'Brave-Matt': 'UB9GJLKDY',
    'bsclifton': 'U13AH4AJY',
    'btlechowski': 'U8M8YQNRJ',
    'cdesouza-chromium': 'U038X9ZBBUZ',
    'cezaraugusto': 'U13AH4AJY',
    'cypt4': 'U03JF90SXU0',
    'darkdh': 'U1M7ELUSV',
    'deeppandya': 'UK2T5MQRM',
    'diracdeltas': 'U0B9C844X',
    'DJAndries': 'U030HSZQANL',
    'Douglashdaniel': 'U01Q1DJGB39',
    'emerick': 'U9E5WAX34',
    'evq': 'U5N5PQACV',
    'fallaciousreasoning': 'U03DL26644V',
    'fmarier': 'UFAJB5HB8',
    'Fanboynz': 'UK7MJJX44',
    'gdregalo': 'U3MLL9K8C',
    'GeetaSarvadnya': 'UAA2QRP17',
    'Genysys': 'ULC9D16TH',
    'goodov': 'U01N082FZ0S',
    'gpestana': 'UK1C3AZMJ',
    'Gyuyoung': 'U0170E17UQL',
    'hollons': 'U7WJA137Y',
    'iambrianfung': 'U01M7GYJFFF',
    'iccub': 'U815AK5JS',
    'iefremov': 'UE87NRK2A',
    'itschrishudson': 'U02DNACM0AU',
    'jamesmudgett': 'U2APFJL5P',
    'jonathansampson': 'U2D8DG0EM',
    'josheleonard': 'U032TFAKQDT',
    'jsecretan': 'U08PTRJT1',
    'jumde': 'U68S7NAFK',
    'justnom': 'U01AS121HUH',
    'karenkliu': 'UB9B8D46Q',
    'kdenhartog': 'U034SEGDUJ3',
    'keur': 'UK776151S',
    'kim0': 'U03EH3082HK',
    'kjozwiak': 'U3MRXKK1Q',
    'kylehickinson': 'UAR38EQTG',
    'LaurenWags': 'U5HCYJGUV',
    'linhkikuchi': 'UKNGLUHC6',
    'LorenzoMinto': 'U01HZL388NB',
    'mariospr': 'U0170E1A3GC',
    'marshall': 'U04PX1BUA',
    'mattmcalister': 'ULEV2H3HT',
    'mbacchi': 'UBU5ZJ5NC',
    'mherrmann': 'U01124T2AHG',
    'mihaiplesa': 'UBU5ZJ5NC',
    'miyayes': 'UB5QY7G93',
    'mkarolin': 'UC4RZJMSB',
    'moritzhaller': 'UM5GQEGBV',
    'mrobinson': 'U0170E1AXRS',
    'muliswilliam': 'U02NUC7L4N4',
    'NejcZdovc': 'U3MLL9K8C',
    'Miyayes': 'UB5QY7G93',
    'nvonpentz': 'U7XHVUZHU',
    'nuo-xu': 'U02GKAHTYGK',
    'onyb': 'U022238N01W',
    'orspetol': 'U01GPJW3QKE',
    'Pavneet-Sing': 'U02Q0MFDNNB',
    'pes10k': 'U5H3AC7LL',
    'petemill': 'U7CQA0TST',
    'pilgrim-brave': 'UD4490KT4',
    'qamarngr': 'U03A448GSSK',
    'rebron': 'UBYNQGBUG',
    'ryanbr': 'UK7MJJX44',
    'ryanml': 'U04PX1BUA',
    'samartnik': 'U6GV4FVD4',
    'SergeyZhukovsky': 'U0D73ULKD',
    'ShivanKaul': 'U02031KK8SY',
    'StephenHeaps': 'U035VT5977U',
    'simonhong': 'U9V31L3L0',
    'soner-yuksel': 'U01DVT6HXBR',
    # taher
    'lukemulks': 'U13GWEVHC',
    'nullhook': 'U026CDKRQ83',
    'rillian': 'U02DMCPEGLA',
    'sangwoo108': 'U03HUPSR9H8',
    'spylogsster': 'U01LH63CLTD',
    'srirambv': 'U1U85R2ES',
    'stephendonner': 'U01JEJCV4N7',
    'szilardszaloki': 'U022SK1KS8J',
    'supermassive': 'U036V67RJG3',
    'thypon': 'U02GP6QKR9P',
    'timchilds': 'U030V903WR1',
    'remusao': 'U01NG0QUUH3',
    'tapanmodh': 'U02QX4CFA2K',
    'tomlowenthal': 'U0B9C844X',
    'tmancey': 'UB9PF4X5K',
    'Uni-verse': 'U02T6MGGUGM',
    'v-kat': 'U0317QSR94H',
    'wchen342': 'U01PRHY091A',
    'wknapik': 'U01PAAE67FZ',
    'yachtcaptain23': 'UAFGJQ602',
    'yrliou': 'U88QJKZBP',
    'zenparsing': 'UU7NY6Q9L',
}

if (os.getenv('GITHUB_SLACK_MAP_FILE', '')):
    try:
        filename = os.getenv('GITHUB_SLACK_MAP_FILE')
        with open(filename, "r") as fh:
            dynamic_github_slack_mapping = json.load(fh)
        if dynamic_github_slack_mapping:
            github_slack_map = {**dynamic_github_slack_mapping, **github_slack_map}
    except FileNotFoundError:
        print('Warning: GITHUB_SLACK_MAP_FILE is set, but thie file could not be found!')
    except json.JSONDecodeError:
        print('Warning: Error encountered while trying to decode mapping file as json!')

branch_regex = r'^1\.[1-9]\d*\.x+$'

brave_core_milestone_ids_to_version = {v: k for k, v in version_to_brave_core_milestone_ids.items()}
brave_browser_milestone_ids_to_version = {v: k for k, v in version_to_brave_browser_milestone_ids.items()}
slack_github_map = {v: k for k, v in github_slack_map.items()}
