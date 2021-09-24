from gendiff.parsing import parsing
from gendiff.make_dicts import make_dicts


def generate_diff(file1, file2):
    dict_f1, dict_f2 = make_dicts(file1, file2)

    added_keys, deleted_keys, unmodified_keys, \
        modified_keys, sorted_list_of_keys = parsing(dict_f1, dict_f2)

    result_string = '{'
    for key in sorted_list_of_keys:
        if key in added_keys:
            result_string += f'\n  + {key}: {dict_f2[key]}'
        elif key in deleted_keys:
            result_string += f'\n  - {key}: {dict_f1[key]}'
        elif key in unmodified_keys:
            result_string += f'\n    {key}: {dict_f1[key]}'
        elif key in modified_keys:
            result_string += f'\n  - {key}: {dict_f1[key]}'
            result_string += f'\n  + {key}: {dict_f2[key]}'
    result_string += '\n}'

    result_string = result_string.replace("True", "true")
    result_string = result_string.replace("False", "false")

    return result_string
