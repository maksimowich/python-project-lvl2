def convert_status(status):
    if status == "unmodified_only_key" or status == "unmodified_with_value":
        return " "
    elif status == "added":
        return "+"
    elif status == "deleted" or status == "modified":
        return "-"


def get_str_of_deleted_or_added(value, level, str_of_value=''):
    if not isinstance(value, dict):
        return f"{value}\n"
    if isinstance(value, dict):
        str_of_value += "{\n"
        for key, value in value.items():
            str_of_value += "    " * (level + 2) + f"{key}: "
            str_of_value += get_str_of_deleted_or_added(value, level + 1)
        str_of_value += "    " * (level + 1) + "}\n"
    return str_of_value


def stylish(diff):
    def walk(diff, level=0, result_str=""):
        result_str += "{\n"
        list_of_keys = sorted(list(diff.keys()))
        for key in list_of_keys:
            value = diff[key]
            status_in_sign = convert_status(value[0])
            result_str += "    " * level + f"  {status_in_sign} {key}: "
            if value[0] == "unmodified_only_key":
                result_str = walk(value[1], level + 1, result_str)
            elif value[0] in {"added", "deleted", "unmodified_with_value"}:
                result_str += get_str_of_deleted_or_added(value[1], level)
            elif value[0] == "modified":
                result_str += get_str_of_deleted_or_added(value[1][0], level)
                result_str += "    " * level + f"  + {key}: "
                result_str += get_str_of_deleted_or_added(value[1][1], level)
        result_str += level * "    " + "}\n"
        return result_str
    return walk(diff)[:-1]
