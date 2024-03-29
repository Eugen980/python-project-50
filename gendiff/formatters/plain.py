from gendiff.consts import DIFF_TYPES


def to_str(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def get_plain_result_item(item, path=''):
    actual_key = item.get('name')
    actual_path = f"{path}.{actual_key}" if path else actual_key
    action = item.get('action')
    new_value = to_str(item.get('new_value'))
    old_value = to_str(item.get('old_value'))

    match action:
        case DIFF_TYPES.ADDED:
            return f"Property '{actual_path}' was added with value: {new_value}"
        case DIFF_TYPES.DELETED:
            return f"Property '{actual_path}' was removed"
        case DIFF_TYPES.MODIFIED:
            return (
                f"Property '{actual_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        case DIFF_TYPES.NESTED:
            children = item.get('children')
            return format_plain(children, actual_path)
        case DIFF_TYPES.UNCHANGED:
            pass
        case _:
            raise TypeError


def format_plain(diff, path=''):
    result = []
    for item in diff:
        formatted_item = get_plain_result_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)
