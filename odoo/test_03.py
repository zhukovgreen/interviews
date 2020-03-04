from typing import List

import pytest


def int_or_zero(item: str) -> int:
    try:
        return int(item)
    except ValueError:
        return 0


def solution(strings: List[str]) -> int:
    return sum(map(int_or_zero, strings))


def solution_recursive(strings: List[str]) -> int:
    def solve_recursively(remaining_strings: List[str]):
        if len(remaining_strings) == 1:
            return int_or_zero(remaining_strings.pop())
        last_item = int_or_zero(remaining_strings.pop())
        return last_item + solve_recursively(remaining_strings)

    return solve_recursively(strings)


@pytest.mark.parametrize(
    ("strings", "exp"),
    [
        (["a", "5", "6", "b"], 11),
        (["a", "b"], 0),
        (["a", "b", "0"], 0),
        (["5", "a", "b", "6"], 11),
        (["55", "a", "b"], 55),
        (["-55", "a", "b"], -55),
        (["55.5", "a", "b"], 0),
        (["55a", "a", "b"], 0),
    ],
)
def test_solution(strings, exp):
    assert solution(strings) == exp
    assert solution_recursive(strings) == exp
