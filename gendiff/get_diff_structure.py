def get_value_by_path(tree1, path):
    for key in path:
        tree1 = tree1.get(key)
        if tree1 is None:
            return "Отсутствие значения"
    return tree1


def add_key_in_diff(given_key, value, path, status, node_of_diff):
    for key in path:
        node_of_diff = node_of_diff.get(key)[1]
    node_of_diff[given_key] = (status, value)


def get_diff_structure(tree1, tree2):
    diff = {}

    def walk(tree2_node, path=[]):
        for key, tree2_value in tree2_node.items():
            tree1_value = get_value_by_path(tree1, path + [key])
            if tree2_value == tree1_value:
                add_key_in_diff(key, tree2_value,
                                path, "unmodified_with_value", diff)
            elif tree1_value == "Отсутствие значения":
                add_key_in_diff(key, tree2_value, path, "added", diff)
            elif not isinstance(tree1_value, dict)\
                    or not isinstance(tree2_value, dict):
                add_key_in_diff(key, (tree1_value, tree2_value),
                                path, "modified", diff)
            elif isinstance(tree1_value, dict)\
                    and isinstance(tree2_value, dict):
                add_key_in_diff(key, {}, path, "unmodified_only_key", diff)
                walk(tree2_value, path + [key])
        tree1_node = get_value_by_path(tree1, path)
        if isinstance(tree1_node, dict):
            for del_key in (set(tree1_node.keys()) - set(tree2_node.keys())):
                add_key_in_diff(del_key, tree1_node[del_key],
                                path, "deleted", diff)
    walk(tree2)
    return diff
