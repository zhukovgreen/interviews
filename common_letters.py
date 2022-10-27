from functools import partial

import pytest


def longest_chain_of_words(
    inputs: tuple[str, ...],
) -> int:
    """Find the longest chain of words within an array matching the rule.

    The rule is:

    Removing one character from a word, gives you a new word
    which is in the remaining part of the array of words.

    Example:
        Array:
            ("a", "b", "ba", "bca", "bda", "bdca")
        Answer is 4, because:
        bd~c~a == bda (present in the array),  +1 to the chain
        b~d~a == ba, +1 to the chain
        b~a~ == b, +1 to the chain
        chain length is 4
    """
    assert inputs, "expect not empty tuple of strings"
    inputs_sorted = sorted(inputs, key=len)

    def get_longest_path(
        chain: str,
        chains: list[str],
        current_level: int,
        max_level: int,
    ) -> int:
        if len(chain) == 1 or len(chains) == 0:
            return max_level

        def slice_and_join(idx: int) -> str:
            return chain[:idx] + chain[idx + 1 :]

        def exists_in_chains(chain_candidate: str) -> bool:
            return chain_candidate in chains

        try:
            return max(
                map(
                    partial(
                        get_longest_path,
                        chains=chains,
                        current_level=current_level + 1,
                        max_level=max(current_level + 1, max_level),
                    ),
                    filter(
                        exists_in_chains,
                        map(slice_and_join, range(len(chain))),
                    ),
                )
            )
        except ValueError:
            return get_longest_path(chains.pop(), chains, 1, max_level)

    return get_longest_path(inputs_sorted.pop(), inputs_sorted, 1, 1)


@pytest.mark.parametrize(
    ("inputs", "exp"),
    (
        (("a", "b", "ba", "bca", "bda", "bdca"), 4),
        (("a", "b", "ba", "bca", "bdca", "bda"), 4),
        (("a", "b", "bac", "bca", "bda", "bdca"), 2),
        (("a", "b", "and", "an", "bac", "bca", "bda", "bdca"), 3),
        (("a", "and", "an", "bear"), 3),
        (("a", "b"), 1),
        (("a", "a"), 1),
        (("x", "yz"), 1),
        (("x",), 1),
        (("x", "xz"), 2),
        (("xz", "x"), 2),
    ),
)
def test_case(inputs, exp):
    assert longest_chain_of_words(inputs) == exp
