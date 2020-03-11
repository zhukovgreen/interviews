"""
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def filtering_f(num: int) -> bool:
    return all(int(d) % 2 == 0 for d in str(num))


def solution():
    return ",".join(map(str, filter(filtering_f, range(1000, 3000))))


def test_solution():
    print(solution())
    assert "2222" in solution()
