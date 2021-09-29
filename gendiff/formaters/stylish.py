def convert_status(status):
    if status == "unmodified":
        return " "
    elif status == "added":
        return "+"
    elif status == "deleted" or status == "modified":
        return "-"


def get_string_of_deleted_or_added(value, level, string_of_value=''):
    if not isinstance(value, dict):
        return f"{value}\n"
    if isinstance(value, dict):
        string_of_value += "{\n"
        for key, value in value.items():
            string_of_value += "    " * (level + 2) + f"{key}: "
            string_of_value += get_string_of_deleted_or_added(value, level + 1)
        string_of_value += "    " * (level + 1) + "}\n"
    return string_of_value


def stylish(diff):
    def walk(diff, level=0, result_string=""):
        result_string += "{\n"
        list_of_keys = sorted(list(diff.keys()))
        for key in list_of_keys:
            value = diff[key]
            status_in_sign = convert_status(value[0])
            result_string += "    " * level + f"  {status_in_sign} {key}: "
            if value[0] == "unmodified" and isinstance(value[1], dict):
                result_string = walk(value[1], level + 1, result_string)
            if value[0] == "unmodified" and not isinstance(value[1], dict):
                result_string += f"{value[1]}\n"
            elif value[0] == "added" or value[0] == "deleted":
                result_string += get_string_of_deleted_or_added(value[1], level)
            elif value[0] == "modified":
                result_string += get_string_of_deleted_or_added(value[1][0], level)
                result_string += "    " * level + f"  + {key}: "
                result_string += get_string_of_deleted_or_added(value[1][1], level)
        result_string += level * "    " + "}\n"
        return result_string
    return walk(diff)
