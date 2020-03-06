import pytest


class CategoryTree:
    def __init__(self):
        self.tree_repr: dict = {}

    def add_category(self, category, parent):
        if parent is None:
            self.tree_repr[category] = {}
            return

        def add_to_parent(d: dict, search_key: str):
            for k, v in d.items():
                if k == search_key:
                    if not category in v:
                        v[category] = {}
                    else:
                        raise KeyError

                elif v:
                    return add_to_parent(v, search_key)

        add_to_parent(self.tree_repr, parent)

    def get_children(self, parent):
        def search_parent(d: dict, search_key: str):
            for k, v in d.items():
                if k == search_key:
                    return list(v.keys())
                elif v:
                    return search_parent(v, search_key)
            raise KeyError

        return search_parent(self.tree_repr, parent)


def test_solution():
    c = CategoryTree()
    c.add_category("A", None)
    c.add_category("B", "A")
    c.add_category("C", "A")
    c.add_category("D", "C")
    assert c.get_children("A") == ["B", "C"]
    assert c.get_children("C") == ["D"]
    with pytest.raises(KeyError):
        c.add_category("B", "A")
