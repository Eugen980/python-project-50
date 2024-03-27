from gendiff.consts import ADD, DEL, OFFSET_LEFT, SEP, DIFF_TYPES


def to_str(value, depth=1):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEP * ((depth * OFFSET_LEFT - 2) + OFFSET_LEFT)
        lines = []
        for key, inner_value in value.items():
            formatted_value = to_str(
                inner_value,
                depth + 1
            )
            lines.append(f"{indent}  {key}: {formatted_value}")
        formatted_string = '\n'.join(lines)
        end_indent = SEP * depth * OFFSET_LEFT
        return f"{{\n{formatted_string}\n{end_indent}}}"
    return f"{value}"


def format_stylish(diff, depth=1):
    indent = SEP * (depth * OFFSET_LEFT - 2)
    lines = []
    for item in diff:
        key_name = item['name']
        old_value = to_str(item.get("old_value"), depth)
        new_value = to_str(item.get("new_value"), depth)
        action = item["action"]
        match action:
            case DIFF_TYPES.UNCHANGED:
                current_value = to_str(item.get("value"), depth)
                lines.append(f"{indent}  {key_name}: {current_value}")
            case DIFF_TYPES.MODIFIED:
                lines.append(f"{indent}{DEL} {key_name}: {old_value}")
                lines.append(f"{indent}{ADD} {key_name}: {new_value}")
            case DIFF_TYPES.DELETED:
                lines.append(f"{indent}{DEL} {key_name}: {old_value}")
            case DIFF_TYPES.ADDED:
                lines.append(f"{indent}{ADD} {key_name}: {new_value}")
            case DIFF_TYPES.NESTED:
                children = format_stylish(
                    item.get("children"), depth + 1
                )
                lines.append(f"{indent}  {key_name}: {children}")

    formatted_string = '\n'.join(lines)
    end_indent = SEP * (depth * OFFSET_LEFT - 4)

    return f"{{\n{formatted_string}\n{end_indent}}}"
