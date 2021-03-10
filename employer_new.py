"""

Yes, No, Maybe game checker

You are implementing a game that consists of a series
of decision points for the player. At each decision point
, the player has to respond with one of the following:
Yes, No, or Maybe.
There is a known, finite set of "winning" paths through the game that might look like this:

NNMYNYYMNNNYYYNYYYM
YYYMNYYMNNNY
YYNYYYMMNYYMNNYYNY
YYMMNYYMNNNNYYYN
And so on...

All other sequences of moves not listed are "losing" paths. Your task is to
implement a checker that, given a sequence of moves, determines if the outcome
is "win" or "lose." How would you approach the task?
"""
from typing import Generator, Iterator

WINING_COMBS = (
    "NNY",
    "YYN",
)


def solution_variable_length(user_inp: str) -> bool:
    return any(
        win_comb.startswith(user_inp)
        for win_comb in WINING_COMBS
    )


def solution_equal_length(user_inp: str) -> bool:
    # return any(win_comb.startswith(user_inp) for win_comb in WINING_COMBS)
    return user_inp in WINING_COMBS


def solution_no_python_tree_reduced_complexity(
    user_inp: Iterator[str], tree: dict
) -> bool:
    try:
        char = next(user_inp)
        if char in tree:
            return solution_no_python_tree_reduced_complexity(
                user_inp, tree[char]
            )
        else:
            return False
    except StopIteration:
        return True


def test_tree_solution():
    """
    YYY
    YNN
    YYN
    """
    tree = {
        "Y": {
            "Y": {"Y": {}, "N": {}},
            "N": {"N": {}},
        }
    }
    assert (
        solution_no_python_tree_reduced_complexity(
            iter("YYY"), tree
        )
        is True
    )
    assert (
        solution_no_python_tree_reduced_complexity(
            iter("YNN"), tree
        )
        is True
    )
    assert (
        solution_no_python_tree_reduced_complexity(
            iter("YYN"), tree
        )
        is True
    )
    assert (
        solution_no_python_tree_reduced_complexity(
            iter("NYN"), tree
        )
        is False
    )
    assert (
        solution_no_python_tree_reduced_complexity(
            iter("YNY"), tree
        )
        is False
    )


def test_something():

    user_input = "NNY"
    winning_combs = ("NNN",)
    assert solution(user_input) is False

    user_input = "NNY"
    winning_combs = ("NNY",)
    assert solution(user_input) is True
