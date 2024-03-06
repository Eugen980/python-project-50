from gendiff.parser import parse_data_from_file


def generate_diff(file1, file2):
    data1 = parse_data_from_file(file1)
    data2 = parse_data_from_file(file2)
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
