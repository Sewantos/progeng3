def bubble_sort(arr: list[int]) -> list[list[int]]:
    """Сортирует пузырьком массив чисел по возрастанию."""
    if not arr:
        return []

    n = len(arr)
    states: list[list[int]] = []

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if swapped:
            states.append(arr.copy())
        else:
            if not states:
                states.append(arr.copy())
            break

    return states
