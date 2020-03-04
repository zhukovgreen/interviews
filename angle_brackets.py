def solution(angles: str) -> str:
    level = 0
    prefix = ""
    for c in angles:
        level += c == "<"
        level -= c == ">"
        if level < 0:
            prefix += "<"
            level += 1
    return prefix + angles + level * ">"


def test_angles():
    assert solution("><<><") == "<><<><>>"
