from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_diff(diff, formater):
    if formater == 'stylish':
        return format_stylish(diff)
    if formater == 'plain':
        return format_plain(diff)
    if formater == 'json':
        return format_json(diff)
