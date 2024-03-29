import pytest
from gendiff.generate import generate_diff
from gendiff.consts import FORMATS


def get_fixtures_data(file):
    with open(get_path(file), 'r') as expected:
        return expected.read()


def get_path(filename):
    return f'./tests/fixtures/{filename}'


@pytest.mark.parametrize(
    ['file1', 'file2'],
    [
        ('file1.json', 'file2.json')
    ]
)
def test_generator_diff(file1, file2):
    assert get_fixtures_data('expected_stylish') == generate_diff(get_path(file1), get_path(file2))    # noqa: E501
    assert get_fixtures_data('expected_stylish') == generate_diff(get_path(file1), get_path(file2), formatter=FORMATS.STYLISH)    # noqa: E501
    assert get_fixtures_data('expected_json') == generate_diff(get_path(file1), get_path(file2), formatter=FORMATS.JSON)    # noqa: E501
    assert get_fixtures_data('expected_plain') == generate_diff(get_path(file1), get_path(file2), formatter=FORMATS.PLAIN)    # noqa: E501
