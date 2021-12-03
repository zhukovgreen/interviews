import math
import pathlib
from functools import reduce
from itertools import *
from typing import Tuple

import pytest


def solution_1_0(array: Tuple[int, ...]) -> int:
    res = 0
    if len(array) >= 2:
        for i, j in zip(array[0:-1], array[1:]):
            res += 1 if j > i else 0
        return res
    else:
        return 0


def solution_1_1(array: Tuple[int, ...]) -> int:
    return sum(map(lambda X: 1 if X[0] < X[1] else 0, pairwise(array)))


def solution_2(array: Tuple[int, ...]) -> int:
    def f(x, y):
        return x + (1 if x < y else 0)

    reduce(f, array)


def get_array_from_file(f: pathlib.Path) -> Tuple[int, ...]:
    with open(f) as f:
        return tuple(int(l.strip()) for l in f)


@pytest.mark.parametrize(
    ("sample", "expected"),
    (
        ((5, 8, 19, 25), 3),
        ((1, 2, 3, 4), 3),
        ((1, 2, 3, 2), 2),
        ((1, 2, 3, 2), 2),
        ((), 0),
        ((1,), 0),
        ((2, 1), 0),
        (get_array_from_file(pathlib.Path("task_1.in")), 1446),
    ),
)
def test_solution_1(sample, expected):
    assert solution_1_1(sample) == expected


def solution_2_0(array: Tuple[int, ...]) -> int:
    previous = math.inf
    res = 0
    if len(array) > 3:
        for i, j, k in zip(array[:-2], array[1:-1], array[2:]):
            current = i + j + k
            res += 1 if current > previous else 0
            previous = current
        return res
    else:
        return res


@pytest.mark.parametrize(
    ("sample", "expected"),
    (
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 5),
        (get_array_from_file(pathlib.Path("task_1_2.in")), 1486),
    ),
)
def test_solution_2(sample, expected):
    assert solution_2_0(sample) == expected
