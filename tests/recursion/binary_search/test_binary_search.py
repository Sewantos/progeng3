from tasks.recursion.binary_search.solution import binary_search


def test_empty_array() -> None:
    assert binary_search([], 10) == -1
    assert binary_search([], 0) == -1


def test_single_element() -> None:
    assert binary_search([5], 5) == 0
    assert binary_search([10], 0) == -1
    assert binary_search([-100], -100) == 0


def test_target_not_found() -> None:
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 2) == -1
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 10) == -1
    assert binary_search(arr, 0) == -1


def test_target_found_various_positions() -> None:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 9) == 8
    assert binary_search(arr, 5) == 4
    assert binary_search(arr, 6) == 5


def test_with_duplicates() -> None:
    arr = [1, 2, 2, 2, 2, 3, 4, 5]
    idx = binary_search(arr, 2)
    assert idx in (1, 2, 3, 4)


def test_large_values_and_bounds() -> None:
    arr = [-(10**9), -500000000, 0, 500000000, 10**9]
    assert binary_search(arr, -(10**9)) == 0
    assert binary_search(arr, 10**9) == 4
    assert binary_search(arr, 0) == 2
    assert binary_search(arr, 123) == -1


def test_large_array_performance() -> None:
    import random

    random.seed(42)
    arr = sorted(random.randint(-(10**9), 10**9) for _ in range(10**6))
    assert binary_search(arr, arr[500000]) == 500000
    assert binary_search(arr, 9999999999) == -1
