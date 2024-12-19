from collections import deque
from collections.abc import Iterable

import pytest


def solution(array: tuple[int, ...], sum_: int) -> tuple[int, int]:
    def inner(
        array: tuple[int, ...],
        left: int,
        right: int,
    ) -> tuple[int, int]:
        if array[0] + array[-1] == sum_:
            return left, right



    return inner(array, 0, len(array))


@pytest.mark.parametrize(
    ("array", "sum_", "exp"),
    (
        ((1, 2, 3, 4, 6), 6, (1, 3)),
        ((1, 2, 3, 4, 6), 6, (1, 3)),
    ),
)
def test_solution(array, sum_, exp):
    assert solution(array, sum_) == exp
