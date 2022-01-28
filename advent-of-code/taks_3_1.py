import pathlib
from typing import Tuple

import pytest


def solution(array: Tuple[int, ...]) -> int:
    res = 0
    if len(array) >= 2:
        for i, j in zip(array[0:-1], array[1:]):
            res += 1 if j > i else 0
        return res
    else:
        return 0


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
def test_solution(sample, expected):
    assert solution(sample) == expected
