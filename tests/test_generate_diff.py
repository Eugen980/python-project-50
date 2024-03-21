import pytest
from gendiff.generate import generate_diff


def get_fixtures_data(path_to_file):
    with open(path_to_file, 'r') as expected:
        return expected.read()


@pytest.mark.parametrize(
    ['path_to_file1', 'path_to_file2', 'formatter', 'expected_file'],
    [
        (
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json',
            'stylish',
            './tests/fixtures/expected.txt'
        ),
        (
            './tests/fixtures/file1_yaml.yaml',
            './tests/fixtures/file2_yaml.yml',
            'stylish',
            './tests/fixtures/expected.txt'
        ),
        (
            './tests/fixtures/file3.json',
            './tests/fixtures/file4.json',
            'stylish',
            './tests/fixtures/expected2.txt'
        ),
        (
            './tests/fixtures/file3.json',
            './tests/fixtures/file4.json',
            'plain',
            './tests/fixtures/expected_plain.txt'
        ),
        (
            './tests/fixtures/file3.json',
            './tests/fixtures/file4.json',
            'json',
            './tests/fixtures/expected_json.txt'
        )
    ]
)
def test_generator_diff(path_to_file1, path_to_file2, formatter, expected_file):
    result = get_fixtures_data(expected_file)
    assert result == generate_diff(path_to_file1, path_to_file2, formatter)
