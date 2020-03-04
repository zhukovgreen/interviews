import pytest

char_to_idx = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "J": 8,
    "K": 9,
}


def solution(N, S):
    def solve_one_row(occupied: list) -> int:
        if all(seat not in (1, 2, 3, 4, 5, 6, 7, 8) for seat in occupied):
            return 2
        if all(seat not in (1, 2, 3, 4) for seat in occupied):
            return 1
        if all(seat not in (3, 4, 5, 6) for seat in occupied):
            return 1
        if all(seat not in (5, 6, 7, 8) for seat in occupied):
            return 1
        return 0

    seats_map = {str(i): [] for i in range(1, N + 1)}
    for row, char in S.split():
        seats_map[row].append(char_to_idx[char])
    return sum(map(solve_one_row, seats_map.values()))


@pytest.mark.parametrize(
    ("N", "S", "exp"), [(2, "1A 2F 1C", 2), (1, "", 2), (1, "1G 1D", 0)],
)
def test_solution(N, S, exp):
    assert solution(N, S) == exp
