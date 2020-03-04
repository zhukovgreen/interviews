from collections import Counter
from functools import reduce
from operator import add
from typing import List


def solution(dicts: List[dict]) -> dict:
    return dict(reduce(add, map(Counter, dicts)))


def test_sol():
    print(solution([{"a": 1, "b": 2}, {"a": 1, "c": 1}]))
