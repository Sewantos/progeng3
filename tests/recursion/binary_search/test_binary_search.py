import random

import pytest

from tasks.recursion.binary_search.solution import binary_search


@pytest.mark.parametrize(
    "arr, target, expected",
    [
        ([], 10, -1),
        ([], 0, -1),
        ([5], 5, 0),
        ([10], 0, -1),
        ([-100], -100, 0),
        ([1, 3, 5, 7, 9], 2, -1),
        ([1, 3, 5, 7, 9], 4, -1),
        ([1, 3, 5, 7, 9], 10, -1),
        ([1, 3, 5, 7, 9], 0, -1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 8),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 6, 5),
        ([-(10**9), -500_000_000, 0, 500_000_000, 10**9], -(10**9), 0),
        ([-(10**9), -500_000_000, 0, 500_000_000, 10**9], 10**9, 4),
        ([-(10**9), -500_000_000, 0, 500_000_000, 10**9], 0, 2),
        ([-(10**9), -500_000_000, 0, 500_000_000, 10**9], 123, -1),
    ],
)  # type: ignore[misc]
def test_binary_search_basic(
    arr: list[int], target: int, expected: int
) -> None:
    assert binary_search(arr, target) == expected


def test_with_duplicates() -> None:
    arr = [1, 2, 2, 2, 2, 3, 4, 5]
    idx = binary_search(arr, 2)
    assert idx in (1, 2, 3, 4)


def test_large_array_performance() -> None:
    random.seed(42)
    arr = sorted(random.randint(-(10**9), 10**9) for _ in range(10**6))
    assert binary_search(arr, arr[500_000]) == 500_000
    assert binary_search(arr, 9999999999) == -1
