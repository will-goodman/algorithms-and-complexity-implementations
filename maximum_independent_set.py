

def maximum_independent_set(tree):
    """
    Given a Tree, computes the Maximum Independent Set at each node

    :param tree: Dictionary representing the tree. Each node is a key and the value is a list of its children.
                 E.g. {'u': ['v', 'x']} means that node u has two children: v and x.
    :return: Dictionary with nodes as keys and the value of their Maximum Independent Set as the value
    """
    max_ind_set = {}
    if len(tree) > 0:
        for vertex in tree.keys():
            children = [x for x in tree.get(vertex)]
            children_ind_set = len([max_ind_set.get(child) for child in children])

            grandchildren = []
            for child in children:
                grandchildren += [x for x in tree.get(child) if x != vertex]

            grandchildren_ind_set = len([max_ind_set.get(grandchild) for grandchild in grandchildren])

            max_ind_set.update({vertex: max(children_ind_set, 1 + grandchildren_ind_set)})

    return max_ind_set


tree = {
    'a': ['b', 'e'],
    'b': ['c'],
    'c': [],
    'e': ['f', 'd'],
    'f': [],
    'd': ['g'],
    'g': []
}

max_ind_set = maximum_independent_set(tree)
# Expected: {'a': 4, 'b': 1, 'c': 1, 'e': 2, 'f': 1, 'd': 1, 'g': 1}
print(max_ind_set)
