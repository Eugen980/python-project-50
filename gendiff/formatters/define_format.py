from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain


def format_diff(diff, formater):
    if formater == 'stylish':
        return format_stylish(diff)
    if formater == 'plain':
        return format_plain(diff)
