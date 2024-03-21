from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
    if formatter == 'plain':
        return format_plain(diff)
    if formatter == 'json':
        return format_json(diff)
