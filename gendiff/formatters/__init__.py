from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json
from gendiff.consts import FORMATS


def format_diff(diff, formatter):
    match formatter:
        case FORMATS.STYLISH:
            return format_stylish(diff)
        case FORMATS.JSON:
            return format_json(diff)
        case FORMATS.PLAIN:
            return format_plain(diff)
        case _:
            raise ValueError(f'Invalid format {formatter}')
