from typing import Generator, Union


def solution() -> Generator[Union[int, str], None, None]:
    """Outputs sequentially the integers from 1 to 99.

    But on some conditions prints a string instead:
    when the integer is a multiple of 3 print “Open” instead of the number,
    when it is a multiple of 7 print “Source” instead of the number,
    when it is a multiple of both 3 and 7 print “OpenSource” instead of the number.
"""
    for i in range(1, 100):
        if i % 3 == 0 and i % 7 == 0:
            yield "OpenSource"
        elif i % 3 == 0:
            yield "Open"
        elif i % 7 == 0:
            yield "Source"
        else:
            yield i


def test_solution():
    list_of_vals = list(solution())
    assert list_of_vals[0] == 1
    assert len(list_of_vals) == 99
    assert list_of_vals[3 - 1] == "Open"
    assert list_of_vals[7 - 1] == "Source"
    assert list_of_vals[21 - 1] == "OpenSource"
