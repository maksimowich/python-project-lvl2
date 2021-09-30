def format_(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    else:
        return value


def get_format_changed(dict_):
    for key, value in dict_.items():
        if isinstance(value, dict):
            get_format_changed(value)
        else:
            dict_[key] = format_(value)
    return dict_
