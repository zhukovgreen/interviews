def tuple_slice(startIndex: int, endIndex: int, tup: tuple) -> str:
    return ",".join(map(str, list(tup)[startIndex:endIndex]))


def test_solution():
    assert tuple_slice(1, 4, (76, 34, 13, 64, 12)) == "34,13,64"
    assert tuple_slice(1, 4, (1,)) == "34,13,64"
