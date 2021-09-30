import json
import yaml


def get_dict_from_file(file):
    if file.find(".yml") != -1 or file.find(".yaml") != -1:
        dict_file = yaml.safe_load(open(file))
    elif file.find(".json") != -1:
        dict_file = json.load(open(file))
    return dict_file
