import random
from itertools import pairwise

from tasks.sorts.bubble_sort.solution import bubble_sort


def test_already_sorted() -> None:
    arr = [1, 2, 3, 4, 5]
    assert bubble_sort(arr.copy()) == [[1, 2, 3, 4, 5]]


def test_reverse_sorted() -> None:
    arr = [5, 4, 3, 2, 1]
    expected = [
        [4, 3, 2, 1, 5],
        [3, 2, 1, 4, 5],
        [2, 1, 3, 4, 5],
        [1, 2, 3, 4, 5],
    ]
    assert bubble_sort(arr.copy()) == expected


def test_example_from_task() -> None:
    arr = [3, 7, 9, 4, 3, 1, 8, 5]
    expected = [
        [3, 7, 4, 3, 1, 8, 5, 9],
        [3, 4, 3, 1, 7, 5, 8, 9],
        [3, 3, 1, 4, 5, 7, 8, 9],
        [3, 1, 3, 4, 5, 7, 8, 9],
        [1, 3, 3, 4, 5, 7, 8, 9],
    ]
    assert bubble_sort(arr.copy()) == expected


def test_with_duplicates_and_negatives() -> None:
    arr = [5, -1, 3, 5, -1, 0, 5]
    result = bubble_sort(arr.copy())

    assert result[-1] == [-1, -1, 0, 3, 5, 5, 5]

    prev = None
    for state in result:
        if prev is not None:
            curr_inv = sum(a > b for a, b in pairwise(state))
            prev_inv = sum(p > q for p, q in pairwise(prev))
            assert curr_inv <= prev_inv
        prev = state

    assert len({tuple(state) for state in result}) == len(result)


def test_random_large_array() -> None:
    arr = list(range(1000))
    random.shuffle(arr)
    result = bubble_sort(arr.copy())

    assert result[-1] == list(range(1000))
    assert len(result) <= 999
    assert len({tuple(state) for state in result}) == len(result)


def test_minimum_size_two_elements() -> None:
    assert bubble_sort([1, 2]) == [[1, 2]]
    assert bubble_sort([2, 1]) == [[1, 2]]
