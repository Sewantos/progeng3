import pytest

from tasks.data_structures.stack_max.solution import StackMax


@pytest.mark.parametrize(
    "initial_ops, expected_first_max",
    [
        ([], "None"),
        ([("push", 5)], 5),
        ([("push", 5), ("push", 1)], 5),
        ([("push", 5), ("push", 1), ("push", 10)], 10),
    ],
)  # type: ignore[misc]
def test_push_and_get_max_parametrized(
    initial_ops: list[tuple[str, int]], expected_first_max: int | str
) -> None:
    stack = StackMax()
    for _op, value in initial_ops:
        stack.push(value)
    assert stack.get_max() == expected_first_max


def test_empty_stack_behavior() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"
    assert stack.get_max() == "None"


def test_pop_and_max_update() -> None:
    stack = StackMax()
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.push(7)

    assert stack.get_max() == 7
    stack.pop()
    assert stack.get_max() == 5
    stack.pop()
    assert stack.get_max() == 5
    stack.pop()
    assert stack.get_max() == 3
    stack.pop()
    assert stack.get_max() == "None"


def test_example_1() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    stack.push(7)
    stack.pop()
    stack.push(-2)
    stack.push(-1)
    stack.pop()
    assert stack.get_max() == -2
    assert stack.get_max() == -2


def test_example_2() -> None:
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    assert stack.pop() == "error"
    stack.push(10)
    assert stack.get_max() == 10
    stack.push(-9)
    assert stack.get_max() == 10


def test_large_values_and_duplicates() -> None:
    stack = StackMax()
    stack.push(100000)
    assert stack.get_max() == 100000
    stack.push(100000)
    assert stack.get_max() == 100000
    stack.pop()
    assert stack.get_max() == 100000
    stack.pop()
    assert stack.get_max() == "None"
