import yaml
import json


def parse_data(extension, data):
    match extension:
        case '.json':
            return json.loads(data)
        case '.yaml' | '.yml':
            return yaml.safe_load(data)
        case _:
            raise NameError('Invalid file format')
