version_to_milestone_ids = {
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
}

closed_labels = set([
    'closed/invalid',
    'closed/not-actionable',
    'closed/fixed-by-component-update',
    'duplicate',
])

branch_regex = r'^1\.\d+\.x+$'

milestone_ids_to_version = {v: k for k, v in version_to_milestone_ids.items()}
