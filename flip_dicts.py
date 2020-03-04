from typing import List, Dict

import pytest


def solution(input: Dict[str, List[str]]) -> dict:
    res = {}
    for k in sorted(input):
        for i in input[k]:
            res.setdefault(i, []).append(k)
    return dict(res)


@pytest.mark.parametrize(
    ("input", "exp"),
    [
        (
            {
                "c": ["d", "b"],
                "a": ["b", "c"],
                "e": ["f",],
            },
            {
                "b": ["a", "c"],
                "c": ["a",],
                "d": ["c",],
                "f": ["e",],
            },
        ),
    ],
)
def test_solution(input, exp):
    assert solution(input) == exp
