def get_string_for_path(path):
    return ".".join(path)


def get_right_format_for_value(value):
    if value == "false" or value == "true" or value == "null" or isinstance(value, int):
        return value
    else:
        return f"\'{value}\'"


def get_string_for_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    else:
        return get_right_format_for_value(value)

def get_string_for_added(path, value):
    string_for_path = get_string_for_path(path)
    string_for_value = get_string_for_value(value)
    return f"Property \'{string_for_path}\' was added with value: {string_for_value}\n"


def get_string_for_deleted(path):
    string_for_path = get_string_for_path(path)
    return f"Property \'{string_for_path}\' was removed\n"


def get_string_for_modified(path, value):
    string_for_path = get_string_for_path(path)
    string_for_deleted_value = get_string_for_value(value[0])
    string_for_added_value = get_string_for_value(value[1])
    return f"Property \'{string_for_path}\' was updated. From {string_for_deleted_value} to {string_for_added_value}\n"


def plain(diff):
    def walk(diff, result_string="", path=[]):
        sorted_list_of_keys = sorted(list(diff.keys()))
        for key in sorted_list_of_keys:
            value = diff[key]
            if value[0] == "unmodified" and isinstance(value[1], dict):
                result_string = walk(value[1], result_string, path + [key])
            elif value[0] == "added":
                result_string += get_string_for_added(path + [key], value[1])
            elif value[0] == "deleted":
                result_string += get_string_for_deleted(path + [key])
            elif value[0] == "modified":
                result_string += get_string_for_modified(path + [key], value[1])
        return result_string
    return walk(diff)
