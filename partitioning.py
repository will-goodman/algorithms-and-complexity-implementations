

def partition(distinct_numbers):
    """
    Performs a greedy algorithm to solve the Partitioning problem on a list of distinct real numbers

    :param distinct_numbers: The list of distinct real numbers
    :return: List of pairings of numbers such that the maximum sum of two numbers in a pair is minimized
    """
    pairings = []
    if len(distinct_numbers) % 2 == 0:
        list.sort(distinct_numbers)

        middle_point = int(len(distinct_numbers) / 2)
        first_half = distinct_numbers[:middle_point]
        second_half = distinct_numbers[middle_point:]
        second_half.reverse()

        pairings = tuple(zip(first_half, second_half))

    return pairings


distinct_numbers = [23, 9, -6, 11, -10, 2, 4, 7]
pairings = partition(distinct_numbers)
# Expected: [(-10, 23), (-6, 11), (2, 9), (4, 7)]
print(pairings)
