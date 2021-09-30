import json
from gendiff.formaters.plain import get_str_for_path


def get_dict_for_json(diff):
    dict_for_json = {}

    def walk(diff, path=[]):
        for key, value in diff.items():
            if value[0] == "unmodified_only_key":
                walk(value[1], path + [key])
            else:
                path_str = get_str_for_path(path + [key])
                dict_for_json.setdefault(value[0], {})[path_str] = value[1]
    walk(diff)
    return dict_for_json


def get_json(diff):
    return json.dumps(get_dict_for_json(diff), indent=4)
