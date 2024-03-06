import yaml
import json
import os


def get_extension_file(path_to_file):
    file_name, file_extension = os.path.splitext(path_to_file)
    return file_extension


def get_data_from_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()


def parse_data(extension, data):
    if extension == '.json':
        return json.loads(data)
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(data)


def parse_data_from_file(path_to_file):
    extension = get_extension_file(path_to_file)
    data = get_data_from_file(path_to_file)
    return parse_data(extension, data)
