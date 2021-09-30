from gendiff.gendiff import generate_diff


def test_generate_diff_3():
    path_ex = 'tests/fixtures/test_generate_diff_3/expected_result'
    path_1 = 'tests/fixtures/test_generate_diff_3/file1.json'
    path_2 = 'tests/fixtures/test_generate_diff_3/file2.json'
    excepted_result = open(path_ex, 'r').read()
    assert generate_diff(path_1, path_2, "plain") == excepted_result