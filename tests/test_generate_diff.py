import pytest
from gendiff.generate import generate_diff


def get_fixtures_data(file):
    with open(get_path(file), 'r') as expected:
        return expected.read()


def get_path(filename):
    return f'./tests/fixtures/{filename}'


@pytest.mark.parametrize(
    ['file1', 'file2'],
    [
        (get_path('file3.json'), get_path('file4.json'))
    ]
)
def test_generator_diff(file1, file2):
    assert get_fixtures_data('expected2') == generate_diff(file1, file2)
    assert get_fixtures_data('expected2') == generate_diff(file1, file2, formatter='stylish')    # noqa: E501
    assert get_fixtures_data('expected_json') == generate_diff(file1, file2, formatter='json')    # noqa: E501
    assert get_fixtures_data('expected_plain') == generate_diff(file1, file2, formatter='plain')    # noqa: E501
