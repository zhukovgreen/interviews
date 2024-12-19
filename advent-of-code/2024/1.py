import pathlib
from collections import Counter

from friendly_sequences import Seq


def get_distance(pairs: tuple[tuple[int, int], ...]) -> int:
    return (
        Seq(sorted(item[0] for item in pairs))
        .zip(sorted(item[1] for item in pairs))
        .starmap(lambda i, j: abs(i - j))
        .sum()
    )


def split_into_tuple(line: str) -> tuple[int, int]:
    return Seq(line.split()).map(int).to_tuple()


def similarity_score(pairs: tuple[tuple[int, int], ...]) -> int:
    right = Counter((item[1] for item in pairs))

    def get_similarity_score(item: int) -> int:
        return item * right.get(item, 0)

    return Seq((item[0] for item in pairs)).map(get_similarity_score).sum()


def test_real_input_task_1():
    with pathlib.Path("1.input").open() as fd:
        pairs = (
            Seq(fd)
            .filter(lambda line: bool(line))
            .map(split_into_tuple)
            .to_tuple()
        )
    assert get_distance(pairs) == 1579939


def test_real_input_task_1_1():
    with pathlib.Path("1.input").open() as fd:
        pairs = (
            Seq(fd)
            .filter(lambda line: bool(line))
            .map(split_into_tuple)
            .to_tuple()
        )
    assert similarity_score(pairs) == 20351745
