import numpy as np


def interval_scheduling(requests):
    """
    Performs a greedy algorithm to solve the Interval Scheduling problem on a list of requests

    :param requests: List of tuples representing requests, where the first element is the start time and the second is
                     the end time e.g. (0, 6) starts at time 0 and finishes at time 6
    :return: List of optimum requests such that the number of requests is maximised without clashing
    """
    requests = sorted(requests, key=lambda x: x[1])
    selected_requests = []
    while len(requests) > 0:
        selected_request_start = requests[0][0]
        selected_request_end = requests[0][1]
        selected_requests.append(requests[0])

        requests_to_remove = []
        for request in requests:
            current_request_start = request[0]
            current_request_end = request[1]
            if not (current_request_start < selected_request_start and current_request_end < selected_request_start) \
               and not (current_request_start > selected_request_end and current_request_end > selected_request_end):
                requests_to_remove.append(request)
        requests = [x for x in requests if x not in requests_to_remove]

    return selected_requests


def weighted_interval_scheduling(requests):
    requests = sorted(requests, key=lambda x: x[1])
    requests.insert(0, (0, 0, 0))
    last_compatible_requests = _calculate_last_compatible_requests(requests)
    print(len(requests))
    print(last_compatible_requests)

    max_weights = np.zeros(len(requests))
    selected_requests = []
    for j in range(1, len(requests)):
        max_weight = requests[j][2] + max_weights[last_compatible_requests[j]]
        if max_weight < max_weights[j - 1]:
            max_weights[j] = max_weights[j - 1]
        else:
            print(requests[j], last_compatible_requests[j])
            max_weights[j] = max_weight
            selected_requests = _get_selected_requests(last_compatible_requests, requests, j)
        print(j, max_weights[j], selected_requests)
    print(selected_requests)

    return max_weights


def _calculate_last_compatible_requests(requests):
    last_compatible_requests = []
    for request in requests:
        previous_requests = [previous_request for previous_request in requests if previous_request[1] <= request[0]]
        if len(previous_requests) > 0:
            last_compatible_requests.append(requests.index(previous_requests.pop()))
        else:
            last_compatible_requests.append(None)

    return last_compatible_requests


def _get_selected_requests(last_compatible_requests, requests, current_request):
    selected_requests = [requests[current_request]]
    last_compatible_request = last_compatible_requests[current_request]
    while last_compatible_request != 0:
        # print(last_compatible_request)
        selected_requests.append(requests[last_compatible_request])
        last_compatible_request = last_compatible_requests[last_compatible_request]

    selected_requests.reverse()
    return selected_requests


requests = [(0, 6), (7, 8), (0, 1), (2, 3), (4, 5), (6, 9), (0, 2), (3, 4), (6, 7)]
selected_requests = interval_scheduling(requests)
# Expected: [(0, 1), (2, 3), (4, 5), (6, 7)]
print(selected_requests)

requests = [(0, 6, 3), (7, 8, 2), (0, 1, 5), (2, 3, 1), (4, 5, 2), (6, 9, 3), (0, 2, 4), (3, 4, 2), (6, 7, 3)]
max_weight = weighted_interval_scheduling(requests)
print(max_weight)
