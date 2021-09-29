import json
import yaml


def format_(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    else:
        return value


def make_format_changes(dict_):
    for key, value in dict_.items():
        if isinstance(value, dict):
            make_format_changes(value)
        else:
            dict_[key] = format_(value)


def get_dicts_from_files(f1, f2):
    if f1.find(".yml") != -1 or f1.find(".yaml") != -1:
        dict_f1 = yaml.safe_load(open(f1))
    elif f1.find(".json") != -1:
        dict_f1 = json.load(open(f1))

    if f2.find(".yml") != -1 or f2.find(".yaml") != -1:
        dict_f2 = yaml.safe_load(open(f2))
    elif f2.find(".json") != -1:
        dict_f2 = json.load(open(f2))
    make_format_changes(dict_f1)
    make_format_changes(dict_f2)
    return dict_f1, dict_f2
