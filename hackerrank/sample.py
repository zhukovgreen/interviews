import pytest


def solution(s: str, n: int) -> int:
    if "a" not in s:
        return 0
    s_len = len(s)
    return s.count("a") * (n // s_len) + s[: n % s_len].count("a")


@pytest.mark.parametrize(("S", "n", "exp"), [("abcac", 10, 4), ("aba", 10, 7)])
def test_solution(s, n, exp):
    assert solution(s, n) == exp
