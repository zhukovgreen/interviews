from __future__ import annotations

import random

import pytest


def sum_[T](e: tuple[T]) -> T:
    return sum(e)


def get_parent_idx(
    item_idx: int,
) -> int:
    if item_idx == 0:
        return 0
    return int((item_idx - 1) / 2) if item_idx // 2 != 0 else int((item_idx - 2) / 2)


def get_child_idx(
    item_idx: int,
    max_idx: int,
) -> tuple[int, int]:
    return min(2 * item_idx + 1, max_idx), min(2 * item_idx + 2, max_idx)


def up_heap(heap: list, item_idx: int) -> list:
    parent_idx = get_parent_idx(item_idx)
    if parent_idx == item_idx:
        return heap
    if heap[item_idx] < heap[parent_idx]:
        heap[parent_idx], heap[item_idx] = heap[item_idx], heap[parent_idx]
        return up_heap(heap, parent_idx)
    return heap


def down_heap(heap: list, item_idx: int) -> list:
    left_child_idx, right_child_idx = get_child_idx(item_idx, len(heap) - 1)
    if left_child_idx == right_child_idx == item_idx:
        return heap

    if heap[left_child_idx] < heap[right_child_idx]:
        min_idx = left_child_idx
    else:
        min_idx = right_child_idx

    if heap[item_idx] > heap[min_idx]:
        heap[min_idx], heap[item_idx] = heap[item_idx], heap[min_idx]
        return down_heap(heap, min_idx)
    return heap


def heapify(array: list[float]) -> list[float]:
    heap = []
    for item in array:
        heap.append(item)
        item_idx = len(heap) - 1
        up_heap(heap, item_idx)
    return heap


def heapsort(array: tuple[float, ...]) -> tuple[float, ...]:
    heap = heapify(list(array))
    sorted_array: list[float] = []

    def sortify(heap: list[float]) -> list[float]:
        if not heap:
            return sorted_array
        if len(heap) == 1:
            return sorted_array + heap
        sorted_array.append(heap[0])
        heap[0] = heap.pop()
        heap = down_heap(heap, 0)

        return sortify(heap)

    return tuple(sortify(heap))


def merge_sort(array: list[float]) -> list[float]:
    if not array or len(array) == 1:
        return array

    def merge(left: list[float], right: list[float]) -> list[float]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    split = len(array) // 2
    left_sorted = merge_sort(array[:split])
    right_sorted = merge_sort(array[split:])

    return merge(left_sorted, right_sorted)


@pytest.mark.parametrize(
    ("array", "exp"),
    (
        ((10, 8, 9, 6, 7, 2, 4, 5, 3, 1), (1, 2, 3, 4, 5)),
        # ((2, 4, 5, 3, 1), (1, 2, 3, 4, 5)),
        # ((), ()),
        # ((1,), (1,)),
        # ((4, 4, 5, 3, 1), (1, 3, 4, 4, 5)),
    ),
)
def test_solution(array, exp):
    # assert heapsort(array) == exp
    assert merge_sort(list(array)) == exp


def test_performance():
    import timeit

    print(
        timeit.Timer(
            lambda: heapsort((random.random() * 1000 for _ in range(500)))
        ).timeit(1000)
    )
    print(
        timeit.Timer(
            lambda: sorted((random.random() * 1000 for _ in range(500)))
        ).timeit(1000)
    )
