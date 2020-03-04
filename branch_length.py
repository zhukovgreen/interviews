MAX_ITER = 1000


def solution(arr):
    # Type your solution here
    arr = [i for i in arr if i != -1]

    def traverse(parent, score):
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        try:
            left_child_score = arr[left_child]
        except IndexError:
            return score
        else:
            right_child_score = (
                arr[right_child] if right_child <= len(arr) - 1 else 0
            )
            return traverse(
                left_child, score + left_child_score + right_child_score
            )

    try:
        left_branch_score = traverse(1, arr[1])
        right_branch_score = traverse(2, arr[2])
    except IndexError:
        return ""
    if left_branch_score == right_branch_score:
        return ""
    elif left_branch_score > right_branch_score:
        return "Left"
    else:
        return "Right"


if __name__ == "__main__":
    # solution([3, 6, 2, 9, -1, 10])
    solution([1, 4, 100, 5])
