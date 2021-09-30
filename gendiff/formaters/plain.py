def get_str_for_path(path):
    return ".".join(path)


def get_right_format_for_value(value):
    if value in {"false", "true", "null"} or isinstance(value, int):
        return value
    else:
        return f"\'{value}\'"


def get_str_for_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    else:
        return get_right_format_for_value(value)


def get_str_for_added(path, value):
    str_for_path = get_str_for_path(path)
    str_for_value = get_str_for_value(value)
    return f"Property \'{str_for_path}\' was " + \
           f"added with value: {str_for_value}\n"


def get_str_for_deleted(path):
    str_for_path = get_str_for_path(path)
    return f"Property \'{str_for_path}\' was removed\n"


def get_str_for_modified(path, value):
    str_for_path = get_str_for_path(path)
    str_for_deleted_value = get_str_for_value(value[0])
    str_for_added_value = get_str_for_value(value[1])
    return f"Property \'{str_for_path}\' was updated. " +\
           f"From {str_for_deleted_value} to {str_for_added_value}\n"


def plain(diff, res="", path=[]):
    sorted_list_of_keys = sorted(list(diff.keys()))
    for key in sorted_list_of_keys:
        value = diff[key]
        if value[0] == "unmodified_only_key":
            res = plain(value[1], res, path + [key])
        elif value[0] == "added":
            res += get_str_for_added(path + [key], value[1])
        elif value[0] == "deleted":
            res += get_str_for_deleted(path + [key])
        elif value[0] == "modified":
            res += get_str_for_modified(path + [key], value[1])
    return res
