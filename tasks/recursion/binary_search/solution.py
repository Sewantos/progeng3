def binary_search(arr: list[int], target: int) -> int:
    """Бинарный поиск в отсортированном по возрастанию массиве."""
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
