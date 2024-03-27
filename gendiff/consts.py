from collections import namedtuple

_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple('FormatChoices',
                     map(str.upper, _FORMAT_VALUES))(*_FORMAT_VALUES)

_DIFF_TYPE_VALUES = ('deleted', 'added', 'nested', 'modified', 'unchanged')
DIFF_TYPES = namedtuple('FormatTypes',
                        map(str.upper, _DIFF_TYPE_VALUES))(*_DIFF_TYPE_VALUES)

_DATA_FORMATS = ('json', 'yaml', 'yml')
DATA_FORMATS = namedtuple('DataFormats',
                          map(str.upper, _DATA_FORMATS))(*_DATA_FORMATS)


ADD = '+'
DEL = '-'
SEP = ' '
OFFSET_LEFT = 4
