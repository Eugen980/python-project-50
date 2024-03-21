def build_diff_tree(data1, data2):
    keys = data1.keys() | data2.keys()
    added = data2.keys() - data1.keys()
    deleted = data1.keys() - data2.keys()
    diff = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in added:
            diff.append(
                {
                    'action': 'added',
                    'name': key,
                    'new_value': value2
                })
        elif key in deleted:
            diff.append(
                {
                    'action': 'deleted',
                    'name': key,
                    'old_value': value1
                })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(
                {
                    'action': 'nested',
                    'name': key,
                    'children': build_diff_tree(value1, value2)
                })
        elif value1 != value2:
            diff.append(
                {
                    'action': 'modified',
                    'name': key,
                    'new_value': value2,
                    'old_value': value1
                })
        else:
            diff.append(
                {
                    'action': 'unchanged',
                    'name': key,
                    'value': value1
                })
    sorted_diff = sorted(diff, key=lambda x: x['name'])
    return sorted_diff
