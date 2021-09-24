from gendiff.gendiff import generate_diff


def test_generate_diff_1():
    excepted_result = open('tests/fixtures/test_generate_diff_1/expected_result', 'r').read()
    assert generate_diff('tests/fixtures/test_generate_diff_1/file1.json', 'tests/fixtures/test_generate_diff_1/file2.json') == excepted_result