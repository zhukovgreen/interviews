import pytest

TABLE_TO_TF = str.maketrans("10", "TF")
TABLE_FROM_TF = str.maketrans("TF", "10")


def solution(S, T):
    s_dec = (
        int(
            S[::-1].translate(TABLE_FROM_TF),
            2,
        )
        if S
        else 0
    )
    t_dec = (
        int(
            T[::-1].translate(TABLE_FROM_TF),
            2,
        )
        if T
        else 0
    )
    res_dec = s_dec + t_dec
    res_bin = "{0:b}".format(res_dec)
    return res_bin[::-1].translate(TABLE_TO_TF) if res_dec else ""


@pytest.mark.parametrize(
    ("inp", "exp_res"),
    ((("TFT", "TFTT"), "FTFFT"),),
)
def test_solution(inp, exp_res):
    assert solution(*inp) == exp_res
