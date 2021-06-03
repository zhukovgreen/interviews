from collections import Counter


def solution(s, t):
    a = sorted(Counter(s).values())
    b = sorted(Counter(t).values())
    return sorted(Counter(s).values()) == sorted(Counter(t).values())


def test_solution():
    assert solution("aad", "bbc") is True
    assert solution("kitty", "perry") is True
    assert solution("kitty", "rrpet") is True
    assert solution("foo", "baa") is True
