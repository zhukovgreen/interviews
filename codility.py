import random
from typing import Optional

import pytest

random.seed(0)

def solution(A: list) -> Optional[int]:
    if not A:
        return
    sorted_a = sorted(A)
    try:
        candidate = next(
            filter(lambda i: i[1] - i[0] > 1, zip(sorted_a[:-1], sorted_a[1:]))
        )
    except StopIteration:
        return max(1, sorted_a[-1] + 1)
    else:
        return max(1, candidate[0] + 1)


@pytest.mark.parametrize(
    ("inp", "exp"),
    [
        ([1, 3, 6, 4, 1, 2], 5),
        ([1, 2, 3], 4),
        ([-501, 502, 33], 1),
        ([1, 1000, 3], 2),
        ([-3, -1], 1),
        ([], None),
        ([-3, -2, -1], 1),
        ([5, 6, 7], 8),
        ([5, 6, 8], 7),
        (random.sample(range(1000), 999), 439),
    ],
)
def test_solution(inp, exp):
    assert solution(inp) == exp
