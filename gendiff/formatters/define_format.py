from gendiff.formatters.stylish import format_stylish


def format_diff(diff, formater):
    if formater == 'stylish':
        return format_stylish(diff)
