def solution(tree: list):
    if not tree:
        return 0

    def level(parent, level_no):
        left_child = 2 * parent + 1

        try:
            tree[left_child]
        except IndexError:
            return level_no
        else:
            return level(left_child, level_no + 1)

    return level(0, 1)


def test_solution():
    assert solution([1, 2, 3, 4, -1, -1, -1]) == 3
    assert solution([1, -1, -1]) == 1
