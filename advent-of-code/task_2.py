import dataclasses
import pathlib
from collections import defaultdict, namedtuple
from typing import Tuple

import pytest


def preprocess(array: Tuple[str, ...]) -> defaultdict:
    d = defaultdict(list)
    for item in array:
        k, v = item.split()
        d[k].append(int(v.strip()))
    return d


def solution_1_0(array: Tuple[str, ...]) -> int:
    d = preprocess(array)
    return sum(d["forward"]) * (sum(d["down"]) - sum(d["up"]))


def get_array_from_file(f: pathlib.Path) -> Tuple[str, ...]:
    with open(f) as f:
        return tuple(l.strip() for l in f)


@pytest.mark.parametrize(
    ("sample", "expected"),
    (
        (
            (
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ),
            150,
        ),
        (get_array_from_file(pathlib.Path("task_2.in")), 1962940),
    ),
)
def test_solution_1(sample, expected):
    assert solution_1_0(sample) == expected


def solution_2_0(array: Tuple[str, ...]) -> int:
    @dataclasses.dataclass
    class Item:
        horizontal: int
        depth: int
    aim = Item(0, 0)
    submarine = Item(0, 0)
    for item in array:
        match item.split():
            case ("forward", points):
                points = int(points)
                submarine.horizontal += points
                submarine.depth += aim.depth * points
            case ("up", points):
                points = int(points)
                aim.depth -= points
            case ("down", points):
                points = int(points)
                aim.depth += points
    return submarine.depth * submarine.horizontal


@pytest.mark.parametrize(
    ("sample", "expected"),
    (
        (
            (
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ),
            900,
        ),
        (get_array_from_file(pathlib.Path("task_2.in")), 1813664422),
    ),
)
def test_solution_2(sample, expected):
    assert solution_2_0(sample) == expected
