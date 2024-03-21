import os
from gendiff.parser import parse_data
from gendiff.build_difference import build_diff_tree
from gendiff.formatters import format_diff


def get_extension_file(path_to_file):
    file_name, file_extension = os.path.splitext(path_to_file)
    return file_extension


def get_data_from_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()


def parse_data_from_file(path_to_file):
    extension = get_extension_file(path_to_file)
    data = get_data_from_file(path_to_file)
    return parse_data(extension, data)


def generate_diff(file1, file2, formatter='stylish'):
    data1 = parse_data_from_file(file1)
    data2 = parse_data_from_file(file2)
    diff = build_diff_tree(data1, data2)
    return format_diff(diff, formatter)
