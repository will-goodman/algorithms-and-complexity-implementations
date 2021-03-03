

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


requests = [(0, 6), (7, 8), (0, 1), (2, 3), (4, 5), (6, 9), (0, 2), (3, 4), (6, 7)]
selected_requests = interval_scheduling(requests)
# Expected: [(0, 1), (2, 3), (4, 5), (6, 7)]
print(selected_requests)
