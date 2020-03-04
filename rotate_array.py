def solution(array: list, idx: int) -> list:
    return array[idx:] + array[:idx]


def test_solution():
    assert solution([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
