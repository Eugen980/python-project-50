from gendiff.parser import parse_data_from_file
from gendiff.sorter_data import sorter
from gendiff.formatters.define_format import format_diff


def generate_diff(file1, file2, formatter='stylish'):
    data1 = parse_data_from_file(file1)
    data2 = parse_data_from_file(file2)
    diff = sorter(data1, data2)
    return format_diff(diff, formatter)
