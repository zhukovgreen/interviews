from collections import Counter


def solution(s: str):
    return " ".join(
        str(i)
        for i, _ in sorted(
            filter(
                lambda i: i[1] % 2 != 0, Counter(map(int, s.split())).items()
            )
        )
    )


def test_solution():
    assert solution("4 4 7 8 10 8") == "7 10"
    assert solution("1 1 1") == "1"
