def compare(str_1, str_2):
    # more than one insertion or deletion happen
    if abs(len(str_1) - len(str_2)) > 1:
        return False

    # check which scenarios applied
    remove_happen = True if len(str_1) - len(str_2) == 1 else False
    insertion_happen = True if len(str_2) - len(str_1) == 1 else False
    replace_might_happen = True if len(str_1) == len(str_2) else False

    if remove_happen:
        # removing a character one by one from a str_1 and compare it to str_2
        # if such cases is smaller or equal to 1 - we're fine
        valid = (
            sum(str_1[:i] + str_1[i + 1 :] == str_2 for i in range(len(str_1)))
            <= 1
        )
        if not valid:
            return False
    if insertion_happen:
        # removing a character one by one from a str_2 and compare it to str_1
        # if such cases is smaller or equal to 1 - we're fine
        valid = (
            sum(str_2[:i] + str_2[i + 1 :] == str_1 for i in range(len(str_2)))
            <= 1
        )
        if not valid:
            return False
    if replace_might_happen:
        # compare chars from str_1 to str_2 and if differnce smaller than 1
        # we're fine
        valid = (
            sum(char_1 != char_2 for char_1, char_2 in zip(str_1, str_2)) <= 1
        )
        if not valid:
            return False

    return True


import pytest


@pytest.mark.parametrize(
    ("str_1", "str_2", "exp"),
    [
        ("pales", "pale", True),
        ("pales", "palesk", True),
        ("pale", "bale", True),
        ("pale", "ple", True),
        ("pale", "bake", False),
        ("pale", "pael", False),
        ("pales", "palesad", False),
    ],
)
def test_main(str_1, str_2, exp):
    assert compare(str_1, str_2) == exp
