from itertools import groupby

import pytest


def solution(S):
    res = ""
    for char, group in groupby(S):
        group_len = len(tuple(group))
        res += f"{str(group_len)}{char}" if group_len > 1 else f"{char}"
    return res


@pytest.mark.parametrize(
    ("inp", "exp_res"),
    (
        ("abaaaabbbaata", "ab4a3b2ata"),
        ("", ""),
    ),
)
def test_solution(inp, exp_res):
    assert solution(inp) == exp_res
