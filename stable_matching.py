

def gale_shapley(x_preferences, y_preferences):
    """
    Performs the Gale-Shapley algorithm to find a stable matching between a set of x's and y's.
    The implementation is x-optimal.

    :param x_preferences: Dictionary with x's as the keys and the values are a list of y's in decreasing order of
                          preference
    :param y_preferences: Dictionary with y's as the keys and the values are a list of x's in decreasing order of
                          preference
    :return: A tuple consisting of the following:
                - a dictionary with x's as the keys and the matched y as the values. None if an error occurs
                - an error message, None if one does not occur
    """
    if _is_valid_input(x_preferences, y_preferences):
        matchings = dict.fromkeys(x_preferences.keys(), None)

        unmatched_x = _get_unmatched_x_has_remaining_offers(matchings, x_preferences)
        while unmatched_x:
            highest_ranked_y = x_preferences.get(unmatched_x)[0]
            x_preferences.get(unmatched_x).remove(highest_ranked_y)

            if highest_ranked_y not in matchings.values():
                matchings.update({unmatched_x: highest_ranked_y})
            else:
                for x, y in matchings.items():
                    if y == highest_ranked_y:
                        highest_ranked_y_preferences = y_preferences.get(highest_ranked_y)
                        if highest_ranked_y_preferences.index(unmatched_x) < highest_ranked_y_preferences.index(x):
                            matchings.update({
                                x: None,
                                unmatched_x: highest_ranked_y
                            })
                        break

            unmatched_x = _get_unmatched_x_has_remaining_offers(matchings, x_preferences)

        return matchings, None

    else:
        return None, 'Invalid input'


def _get_unmatched_x_has_remaining_offers(matchings, x_preferences):
    """
    If an x exists without a match, who has not yet made an offer to every y, then this method will return the value of
    x. If no such x exists, then None is returned instead.

    :param matchings: Dictionary of matchings as they currently stand (x's as keys, y's as values). The value of y is
                      None if the given value of x is currently unmatched
    :param x_preferences: Dictionary with x's as the keys and the values are a list of y's in decreasing order of
                          preference. If a given value of y is missing from the list, then that x has already made an
                          offer to that y. If the list for a given x is empty, then that x has made and offer to every
                          y.
    :return: The value of x if one exists, otherwise None
    """
    for x, y in matchings.items():
        if y is None and len(x_preferences.get(x)) > 0:
            return x
    return None


def _is_valid_input(x_preferences, y_preferences):
    """
    Checks whether a given input is valid.
    To be a valid input, each list of preferences for each x must contain every y and vice-versa.

    :param x_preferences: Dictionary with x's as the keys and the values are a list of y's in decreasing order of
                          preference
    :param y_preferences: Dictionary with y's as the keys and the values are a list of x's in decreasing order of
                          preference
    :return: Whether or not the given input is valid
    """
    ys = set(y_preferences.keys())
    for x, preferences in x_preferences.items():
        if set(preferences) != ys:
            return False

    xs = set(x_preferences.keys())
    for y, preferences in y_preferences.items():
        if set(preferences) != xs:
            return False

    return True


hospital_preferences = {
    'h1': ['s1', 's2', 's3'],
    'h2': ['s2', 's1', 's3'],
    'h3': ['s1', 's2', 's3']
}

student_preferences = {
    's1': ['h2', 'h1', 'h3'],
    's2': ['h1', 'h2', 'h3'],
    's3': ['h1', 'h2', 'h3']
}

matchings, error_message = gale_shapley(hospital_preferences, student_preferences)

# Expected: {'h1': 's1', 'h2': 's2', 'h3': 's3'}
print('Final Matchings', matchings)

hospital_preferences = {
    'h1': ['s3', 's2', 's1', 's4'],
    'h2': ['s4', 's1', 's3', 's2'],
    'h3': ['s1', 's2', 's3', 's4'],
    'h4': ['s1', 's4', 's3', 's2']
}

student_preferences = {
    's1': ['h4', 'h2', 'h3', 'h1'],
    's2': ['h1', 'h2', 'h3', 'h4'],
    's3': ['h1', 'h3', 'h2', 'h4'],
    's4': ['h2', 'h4', 'h3', 'h1']
}

matchings, error_message = gale_shapley(hospital_preferences, student_preferences)

# Expected: {'h1': 's3', 'h2': 's4', 'h3': 's2', 'h4': 's1'}
print('Final Matchings', matchings)


