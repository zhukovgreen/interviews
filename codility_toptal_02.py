import pytest


def solution(garden: list) -> int:
    if len(garden) <= 1:
        return 0
    flag = -1 if garden[0] - garden[1] >= 0 else 1

    bad_cases = 0
    for current_t, next_t in zip(garden[:-1], garden[1:]):
        bad_cases += (
            current_t - next_t <= 0 if flag == -1 else next_t - current_t < 0
        )
        flag *= -1
    return bad_cases


@pytest.mark.parametrize(
    ("inp", "exp"),
    [
        ([5, 4, 3, 2, 6], 1),
        ([3, 7, 4, 5], 0),
        ([5, 5, 5, 5], 2),
        ([], 0),
        ([1], 0),
        ([1, 2, 2, 2, 1], 1),
        ([3, 2, 2, 2, 3], 3),
    ],
)
def test_solution(inp, exp):
    assert solution(inp) == exp
