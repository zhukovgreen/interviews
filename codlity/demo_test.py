from typing import List


def solution(a: List):
    a = sorted(set(a))
    if not (a):
        return 1
    if len(a) == 1:
        return max(1, a[0] - 1)
    for el_0, el_1 in zip(a, a[1:]):
        if el_1 - el_0 > 1:
            return max(1, el_0 + 1)
    else:
        return max(1, el_1 + 1)


def test_solution():
    assert solution([-2, 3, 6, 4, 1, 2]) == 1
    assert solution([0]) == 1
    assert solution([2]) == 1
    assert solution([]) == 1
    assert solution([1, 3, 6, 4, 1, 2]) == 5
    assert solution([1, 2, 3]) == 4
    assert solution([-1, -3]) == 1
