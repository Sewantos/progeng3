import random

import pytest

from tasks.sorts.insertion_sort.solution import insertion_sort


@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        ([42], [42]),
        ([-5], [-5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([2, -1, 2, -1, 0], [-1, -1, 0, 2, 2]),
        ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([9, 5, 1, 4, 3], [1, 3, 4, 5, 9]),
        ([1000, -1000, 1000, -1000], [-1000, -1000, 1000, 1000]),
    ],
)  # type: ignore[misc]
def test_insertion_sort_parametrized(
    data: list[int], expected: list[int]
) -> None:
    assert insertion_sort(data) == expected


def test_random_large() -> None:
    random.seed(42)
    data = [random.randint(-1000, 1000) for _ in range(100)]
    sorted_data = insertion_sort(data)
    assert sorted_data == sorted(data)
