from collections import Counter


def inventory_repr(inventory: dict):
    return (
        "Inventory:\n"
        + "\n".join(
            str(num) + " " + item
            for item, num in {
                k: v
                for k, v in sorted(inventory.items(), key=lambda item: item[1])
            }.items()
        )
        + "\nTotal number of item is: "
        + str(sum(inventory.values()))
    )


def add_inventory(inventory: dict, new_items: list):
    return inventory_repr(Counter(inventory) + Counter(new_items))


def test_solution():
    # assert solution({"coin": 10, "dagger": 2, "bow": 1, "arrow": 91}) == 1
    assert (
        add_inventory(
            {"coin": 10, "dagger": 2, "bow": 1, "arrow": 91},
            ["coin", "arrow", "coin", "magic bowl"],
        )
        == 0
    )


class Shape:
    def __init__(self, width: float, height: float = 0):
        """Rectangular or square shape object.

        If height arg is omitted, it considered to be equal to the width
        (square shape)
        """
        self.width = width
        self.height = height if height else width

    @property
    def content(self):
        return self.width * self.height

    @property
    def circumference(self):
        return 2 * (self.width + self.height)


