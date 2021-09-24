def parsing(dict_f1, dict_f2):
    set_f1 = set(dict_f1)
    set_f2 = set(dict_f2)

    added_keys = set_f2 - set_f1
    deleted_keys = set_f1 - set_f2
    modified_and_unmodified_keys = set_f1 & set_f2
    modified_keys = set()
    unmodified_keys = set()
    for key in modified_and_unmodified_keys:
        if dict_f1[key] == dict_f2[key]:
            unmodified_keys.add(key)
        else:
            modified_keys.add(key)

    sorted_list_of_keys = sorted(list(set_f1 | set_f2))

    return added_keys, deleted_keys, unmodified_keys, \
        modified_keys, sorted_list_of_keys
