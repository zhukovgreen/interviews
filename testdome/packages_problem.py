BP_CONTENT = 5
SP_CONTENT = 1


def minimal_number_of_packages(
    items: int, available_large_packages: int, available_small_packages: int
) -> int:
    big_pkgs = min(items // BP_CONTENT, available_large_packages)
    small_pkgs = min(
        (items - big_pkgs * BP_CONTENT) // SP_CONTENT, available_small_packages
    )
    if big_pkgs * BP_CONTENT + small_pkgs * SP_CONTENT < items:
        return -1
    return big_pkgs + small_pkgs


def test_solution():
    assert minimal_number_of_packages(16, 2, 10) == 8
    assert minimal_number_of_packages(1, 2, 0) == -1
    assert minimal_number_of_packages(6, 2, 0) == -1
    assert minimal_number_of_packages(6, 2, 1) == 2
