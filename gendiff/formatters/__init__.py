from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_diff(diff, formatter):
    match formatter:
        case 'stylish':
            return format_stylish(diff)
        case 'json':
            return format_json(diff)
        case 'plain':
            return format_plain(diff)
        case _:
            raise ValueError(f'Invalid format {formatter}')
