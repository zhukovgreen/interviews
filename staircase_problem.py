from itertools import chain, product, permutations


def possible_steps_combination(n: int):
    ones = (([1] * i) for i in range(n // 1 + 1))
    twos = (([2] * i) for i in range(n // 2 + 1))
    threes = (([3] * i) for i in range(n // 3 + 1))

    return tuple(
        filter(lambda x: sum(chain(*x)) == n, product(ones, twos, threes))
    )


def possible_steps_combination_1(n: int, possible_steps=(1, 2, 3)):
    def solver(left: int, right: int):
        left = solver(left // 2 + 1, left // 2) if left != 2 else [1]
        right = solver(right // 2 + 1, right // 2) if left != 2 else [1]
        return left, right

    return tuple(solver(n // 2 + 1, n // 2))


import pytest


@pytest.mark.parametrize(
    ("num_of_steps", "exp"),
    [
        (1, (([1], [], []),)),
        (2, (([], [2], []), ([1, 1], [], []))),
        (3, (([], [], [3]), ([1], [2], []), ([1, 1, 1], [], []))),
    ],
)
def test_basic(num_of_steps, exp):
    assert possible_steps_combination(num_of_steps) == exp


def test_basic1():
    assert possible_steps_combination_1(9) == []


def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1 :]
        yield from subset_sum(
            remaining, target, partial + [n], partial_sum + n
        )


def test_subset_sum():
    assert list(subset_sum([1, 2, 3], 3)) == 0


def solution_1(n: int):
    ones = tuple(((1,) * i) for i in range(n // 1 + 1))
    twos = tuple(((2,) * i) for i in range(n // 2 + 1))
    threes = tuple(((3,) * i) for i in range(n // 3 + 1))

    result = set()
    for group in permutations((ones, twos, threes), 3):
        result |= set(filter(lambda x: sum(chain(*x)) == n, product(*group)))
    return len(result)


def test_solution():
    assert solution(3) == 1


def staircase(n):
    if n == 1 or n == 0:
        return 1
    elif n == 2:
        return 2

    else:
        return staircase(n - 3) + staircase(n - 2) + staircase(n - 1)


def test_staircase():
    assert staircase(3) == 1


def staircase_combinations(n, result=None):
    if result is None:
        result = []
    if n == 1 or n == 0:
        return [(1,)]
    elif n == 2:
        return [(1, 1), (2,)]
    elif n == 3:
        return [(1, 1, 1), (2, 1), (1, 2), (3,)]

    else:
        return staircase_combinations(n - 1)


def test_staircase_combinations():
    assert staircase_combinations(4) == 1


def solution(strings):
    n = 0
    for idx, pair in enumerate(zip(*strings)):
        if len(set(pair)) != 1:
            break
        else:
            n += 1
    return strings[0][:n] if n else ""


def test_strings():
    assert solution(["abcdef", "adegh", "a"]) == 0
