from gendiff.gendiff import generate_diff


def test_generate_diff_1():
    path_ex = 'tests/fixtures/test_generate_diff_1/expected_result'
    path_1 = 'tests/fixtures/test_generate_diff_1/file1.json'
    path_2 = 'tests/fixtures/test_generate_diff_1/file2.json'
    excepted_result = open(path_ex, 'r').read()
    assert generate_diff(path_1, path_2) == excepted_result


def test_generate_diff_2():
    path_ex = 'tests/fixtures/test_generate_diff_2/expected_result'
    path_1 = 'tests/fixtures/test_generate_diff_2/file1.json'
    path_2 = 'tests/fixtures/test_generate_diff_2/file2.json'
    excepted_result = open(path_ex, 'r').read()
    assert generate_diff(path_1, path_2) == excepted_result


print("All tests have been successfully passed!")
