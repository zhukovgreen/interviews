def word_reverser():
    s = str(input())
    res = []
    for idx, w in enumerate(s.split()):
        if idx % 2 == 0:
            res.append(w[::-1])
        else:
            res.append(w)
    return " ".join(res)


def test_solution():
    assert word_reverser("Abc abc abc") == "cbA abc cba"
