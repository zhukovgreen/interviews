import pytest


def solution(s: str) -> int:
    def solver(
        substring: str,
        global_max: int = 0,
    ):
        registry: dict[str, int] = {}
        current_max = 0
        for num, char in enumerate(substring):
            try:
                registry[char]
            except KeyError:
                registry[char], current_max = num + 1, num + 1
            else:
                return solver(
                    substring[1:],
                    global_max=max(
                        current_max,
                        global_max,
                    ),
                )
        return max(
            current_max,
            global_max,
        )

    return solver(s)


@pytest.mark.parametrize(
    ("s", "exp"),
    (
        ("abcabcbb", 3),
        ("abcdefg", 7),
        ("bbbbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("", 0),
    ),
)
def test_solution(s, exp):
    assert solution(s) == exp
