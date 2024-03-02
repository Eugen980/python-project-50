import json


def generator_diff(file1, file2):
    data1 = json.load(open(file1, 'r'))
    data2 = json.load(open(file2, 'r'))
    result = ''
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)
        if value1 == value2:
            result += f'  {str(key)}: {value1}\n'
        elif value2 is None:
            result += f'- {str(key)}: {value1}\n'
        elif value1 is None:
            result += f'+ {str(key)}: {value2}\n'
        elif value1 != value2:
            result += f'- {str(key)}: {value1}\n'
            result += f'+ {str(key)}: {value2}\n'
    return result
