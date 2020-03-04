import pytest


def solution(A: list) -> int:
    A.sort()
    if not A:
        return 1
    if len(A) == 1:
        return max(A[0] + 1, 1)
    possible_pairs = filter(lambda i: i[1] - i[0] > 1, zip(A[:-1], A[1:]))
    try:
        return max(next(possible_pairs)[0] + 1, 1)
    except StopIteration:
        return max(A[-1] + 1, 1)


@pytest.mark.parametrize(
    ("A", "exp"),
    [([1, 2, 3], 4), ([-1, -3], 1), ([1, 3, 6, 4, 1, 2], 5), ([1], 2)],
)
def test_solution(A, exp):
    assert solution(A) == exp
