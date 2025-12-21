class DoubleConnectedNode:
    value: object
    next: "DoubleConnectedNode | None"
    prev: "DoubleConnectedNode | None"

    def __init__(
        self,
        value: object,
        next: "DoubleConnectedNode | None" = None,
        prev: "DoubleConnectedNode | None" = None,
    ) -> None:
        self.value = value
        self.next = next
        self.prev = prev


def solution(
    head: "DoubleConnectedNode | None",
) -> "DoubleConnectedNode | None":
    if not head:
        return None

    current: DoubleConnectedNode | None = head
    previous: DoubleConnectedNode | None = None

    while current is not None:
        next_node: DoubleConnectedNode | None = current.next
        current.next = previous
        current.prev = next_node
        previous = current
        current = next_node

    return previous
