from gendiff.get_diff_structure import get_diff_structure
from gendiff.get_dicts_from_files import get_dict_from_file
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.get_json import get_json
from gendiff.make_format_changes import get_format_changed


def generate_diff(file1, file2, _format="stylish"):
    if _format in {"stylish", "plain"}:
        dict_f1 = get_format_changed(get_dict_from_file(file1))
        dict_f2 = get_format_changed(get_dict_from_file(file2))
        diff = get_diff_structure(dict_f1, dict_f2)
        if _format == "stylish":
            return stylish(diff)
        elif _format == "plain":
            return plain(diff)[:-1]
    elif _format == "json":
        dict_f1 = get_dict_from_file(file1)
        dict_f2 = get_dict_from_file(file2)
        diff = get_diff_structure(dict_f1, dict_f2)
        return get_json(diff)
