from gendiff.get_diff_structure import get_diff_structure
from gendiff.get_dicts_from_files import get_dicts_from_files
from gendiff.formaters.stylish import stylish


def generate_diff(file1, file2, _format="stylish"):

    dict_f1, dict_f2 = get_dicts_from_files(file1, file2)

    diff = get_diff_structure(dict_f1, dict_f2)

    if _format == "stylish":
        return stylish(diff)
