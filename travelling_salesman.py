import itertools


def dynamic_programming_tsp(city_map):
    """
    Uses a dynamic programming approach to solve the Travelling Salesman Problem

    :param city_map: Dictionary containing the minimum distances from each city to each other city

    :return: the minimum distance to travel from the start city to all other cities and back again
    """
    cities = list(city_map.keys())
    print('Start City:', cities[0])
    opt_distances = {}

    for i in range(1, len(cities)):
        opt_distances.update({frozenset({cities[i]}): {cities[i]: city_map.get(cities[0]).get(cities[i])}})

    for k in range(2, len(cities) + 1):
        for subset in _find_subsets(set(cities[1:]), k):
            for city in subset:
                subset_without_current_city = subset.copy()
                subset_without_current_city.remove(city)

                optimum_previous_distance = min(
                    [opt_distances.get(frozenset(subset_without_current_city)).get(previous_city) +
                     city_map.get(previous_city).get(city) for previous_city in subset_without_current_city])

                if frozenset(subset) in opt_distances:
                    opt_distances.get(frozenset(subset)).update({city: optimum_previous_distance})
                else:
                    opt_distances.update({frozenset(subset): {city: optimum_previous_distance}})

    subset_without_start_city = frozenset(cities[1:])
    min_distance = min([opt_distances.get(subset_without_start_city).get(previous_city) +
                        city_map.get(previous_city).get(cities[0]) for previous_city in subset_without_start_city])
    return min_distance


def _find_subsets(original_set, subset_length):
    """
    Generates all possible subsets of a certain size.
    E.g. original_set = {1, 2, 3}, subset_length = 2, then return [{1, 2}, {1, 3}, {2, 3}]

    :param original_set: The original set to generate subsets from
    :param subset_length: The length of all subsets to generate

    :return: all possible subsets of the given length
    """
    tuples = list(itertools.combinations(original_set, subset_length))
    subsets = [set(original_tuple) for original_tuple in tuples]
    return subsets


graph = {
    's': {'u': 1, 'x': 4, 'v': 2, 'y': 6, 'z': 5},
    'u': {'s': 1, 'v': 3, 'x': 1, 'z': 3, 'y': 3},
    'x': {'y': 2, 'z': 2, 'u': 1, 's': 4, 'v': 2},
    'y': {'s': 6, 'u': 3, 'x': 2, 'v': 4, 'z': 4},
    'v': {'x': 2, 'z': 3, 's': 2, 'u': 3, 'y': 4},
    'z': {'s': 5, 'u': 3, 'x': 2, 'y': 4, 'v': 3}
}

min_distance = dynamic_programming_tsp(graph)
# Expected: 13
print(min_distance)
