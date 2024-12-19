import pytest


def solution(array: tuple[int, ...]) -> tuple[int, int]:
    array_sum = sum(array)
    return array_sum - array[-1], array_sum - array[0]


@pytest.mark.parametrize(
    ("array", "exp"),
    (((1, 3, 5, 7, 9), (16, 24)),),
)
def test_solution(array, exp):
    assert solution(array) == exp
