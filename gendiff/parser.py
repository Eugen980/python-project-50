import yaml
import json
from gendiff.consts import DATA_FORMATS


def parse_data(extension, data):
    match extension:
        case DATA_FORMATS.JSON:
            return json.loads(data)
        case DATA_FORMATS.YML | DATA_FORMATS.YAML:
            return yaml.safe_load(data)
        case _:
            raise TypeError('Invalid file format')
