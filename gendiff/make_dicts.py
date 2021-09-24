import json
import yaml


def make_dicts(f1, f2):
    if f1.find(".yml") != -1 or f1.find(".yaml") != -1:
        dict_f1 = yaml.safe_load(open(f1))
    elif f1.find(".json") != -1:
        dict_f1 = json.load(open(f1))

    if f2.find(".yml") != -1 or f2.find(".yaml") != -1:
        dict_f2 = yaml.safe_load(open(f2))
    elif f2.find(".json") != -1:
        dict_f2 = json.load(open(f2))

    return dict_f1, dict_f2
