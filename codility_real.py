import pytest

MAX_ITERS = 1000000


def solution_0(n):
    m = n + 1
    n_sum_of_digits = sum(map(int, str(n)))
    ITER = 0
    while sum(map(int, str(m))) != n_sum_of_digits:
        m += 1
        ITER += 1
        if ITER > MAX_ITERS:
            return None
    return m


def test_solution():
    assert solution_0(28) == 37
    assert solution_0(0) == 37


def solution_1(A: list, B: list) -> int:
    assert len(A) == len(B)  # given in the task spec
    n = 0
    for idx in range(1, len(A)):
        if sum(A[:idx]) == sum(A[idx:]) == sum(B[:idx]) == sum(B[idx:]):
            n += 1
    return n


@pytest.mark.parametrize(
    ("A", "B", "exp"),
    [
        ([4, -1, 0, 3], [-2, 5, 0, 3], 2),
        ([2, -2, -3, 3], [0, 0, 4, -4], 1),
        ([3, 2, 6], [4, 1, 6], 0),
        ([1, 4, 2, -2, 5], [7, -2, -2, 2, 5], 2),
        # ([], [], 1),
        # ([], [], 1),
    ],
)
def test_solution(A, B, exp):
    assert solution_1(A, B) == exp


from itertools import product


def solution(U: int, L: int, C: list) -> str:
    # write your code in Python 3.6
    first_row_candidates = []
    second_row_candidates = []
    for ci in C:
        if ci == 2:
            first_row_candidates.append((1,))
            second_row_candidates.append((1,))
        elif ci == 0:
            first_row_candidates.append((0,))
            second_row_candidates.append((0,))
        else:
            first_row_candidates.append((0, 1))
            second_row_candidates.append((1, 0))
    first_row_candidates = list(product(*first_row_candidates))
    second_row_candidates = list(product(*second_row_candidates))
    for idx, candidate in enumerate(first_row_candidates):
        if sum(candidate) == U and sum(second_row_candidates[idx]) == L:
            return (
                "".join(map(str, candidate))
                + ","
                + "".join(map(str, second_row_candidates[idx]))
            )
    return "IMPOSSIBLE"


@pytest.mark.parametrize(
    ("U", "L", "C", "exp"),
    [
        (3, 2, [2, 1, 1, 0, 1], "11001,11000"),
        (2, 3, [0, 0, 1, 1, 2], "IMPOSSIBLE"),
        (2, 2, [2, 0, 2, 0], "1010,1010"),
    ],
)
def test_solution(U, L, C, exp):
    assert solution(U, L, C) == exp
