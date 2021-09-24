import json


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    set_f1 = set(f1)
    set_f2 = set(f2)

    added = set_f2 - set_f1
    deleted = set_f1 - set_f2
    modified_and_unmodified = set_f1 & set_f2
    modified = set()
    unmodified = set()
    for key in modified_and_unmodified:
        if f1[key] == f2[key]:
            unmodified.add(key)
        else:
            modified.add(key)

    sorted_list_of_keys = sorted(list(set_f1 | set_f2))

    result_string = ''
    result_string += '{'
    for key in sorted_list_of_keys:
        if key in added:
            result_string += f'\n  + {key}: {f2[key]}'
        elif key in deleted:
            result_string += f'\n  - {key}: {f1[key]}'
        elif key in unmodified:
            result_string += f'\n    {key}: {f1[key]}'
        elif key in modified:
            result_string += f'\n  - {key}: {f1[key]}'
            result_string += f'\n  + {key}: {f2[key]}'
    result_string += '\n}'

    result_string = result_string.replace("True", "true")
    result_string = result_string.replace("False", "false")

    return result_string
