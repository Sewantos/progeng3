import random

from tasks.sorts.insertion_sort.solution import insertion_sort


def test_empty_array() -> None:
    assert insertion_sort([]) == []


def test_single_element() -> None:
    assert insertion_sort([42]) == [42]
    assert insertion_sort([-5]) == [-5]


def test_already_sorted() -> None:
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([-2, -1, 0]) == [-2, -1, 0]


def test_reverse_sorted() -> None:
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]


def test_with_duplicates_and_negatives() -> None:
    assert insertion_sort([2, -1, 2, -1, 0]) == [-1, -1, 0, 2, 2]
    assert insertion_sort([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert insertion_sort([1000, -1000, 1000, -1000]) == [
        -1000,
        -1000,
        1000,
        1000,
    ]


def test_example_from_task() -> None:
    assert insertion_sort([9, 5, 1, 4, 3]) == [1, 3, 4, 5, 9]


def test_random_large() -> None:
    random.seed(42)
    data = [random.randint(-1000, 1000) for _ in range(100)]
    sorted_data = insertion_sort(data)
    assert sorted_data == sorted(data)
