import time


def recursive_fibonacci(n):
    """
    Recursively calculates the nth number in the Fibonacci sequence

    :param n: The position in the Fibonacci sequence to calculate
    :return: The value at position n in the Fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


memo_f = [0, 1]


def memoization_fibonacci(n):
    """
    Calculates the nth number of the Fibonacci sequence recursively, making use of Memoization to remember previously
    calculated values

    :param n: The position in the Fibonacci sequence to calculate
    :return: The value at position n in the Fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if len(memo_f) <= n:
            for i in range(max(len(memo_f), 2), n + 1):
                memo_f.append(memoization_fibonacci(i - 1) + memoization_fibonacci(i - 2))
        return memo_f[n]


def iterative_fibonacci(n):
    """
    Iteratively calculates the nth number of the Fibonacci sequence

    :param n: The position in the Fibonacci sequence to calculate
    :return: The value at position n in the Fibonacci sequence
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]


print(recursive_fibonacci(5))

s = time.time()
print(memoization_fibonacci(5))
e = time.time()
print('Memoization 5 first run:', e - s)

s = time.time()
print(memoization_fibonacci(5))
e = time.time()
print('Memoization 5 second run:', e - s)

print(memoization_fibonacci(10))

print(iterative_fibonacci(5))
print(iterative_fibonacci(10))
