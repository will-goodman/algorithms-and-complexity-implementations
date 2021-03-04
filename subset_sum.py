

def subset_sum(whole_set, max_total_weight):
    """
    Given a set of weights and a maximum bound, finds the optimum subset such that the sum of weights is maximised,
    while being less than or equal to the bound

    :param whole_set: List of weights with no duplicates
    :param max_total_weight: Maximum bound
    :return: The maximum possible sum of weights which is less than or equal to the maximum bound
    """
    max_weights = []
    for i in range(len(whole_set) + 1):
        y_axis = []
        for j in range(max_total_weight + 1):
            if i == 0:
                y_axis.append(0)
            else:
                y_axis.append(None)
        max_weights.append(y_axis)

    for i in range(1, len(whole_set) + 1):
        for j in range(max_total_weight + 1):
            previous_max_weight = max_weights[i - 1][j]
            current_max_weight = whole_set[i - 1] + max_weights[i - 1][j - whole_set[i - 1]]
            if 0 <= current_max_weight <= j:
                max_weights[i][j] = max(previous_max_weight, current_max_weight)
            else:
                max_weights[i][j] = previous_max_weight

    return max_weights[len(whole_set)][max_total_weight]


whole_set = [25, 15, 10, 20, 5]
max_total_weight = 35
max_weight = subset_sum(whole_set, max_total_weight)
# Expected: 35
print(max_weight)
