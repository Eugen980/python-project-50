import pytest
from gendiff.generator import generate_diff


@pytest.mark.parametrize(
    ['path_to_file1', 'path_to_file2', 'expected_file'],
    [
        ('./tests/fixtures/file1.json',
         './tests/fixtures/file2.json',
         './tests/fixtures/expected.txt'
         ),
         ('./tests/fixtures/file1_yaml.yaml',
         './tests/fixtures/file2_yaml.yml',
         './tests/fixtures/expected_yaml.txt'
         )
    ]
)
def test_generator_diff(path_to_file1, path_to_file2, expected_file):
    with open(expected_file, 'r') as expected:
        result = expected.read()
    assert result == generate_diff(path_to_file1, path_to_file2)
