class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    """Разворачивает двусвязный список на месте."""
    if not node:
        return node

    current = node
    previous = None

    while current is not None:
        next_node = current.next

        current.next = previous
        current.prev = next_node

        previous = current
        current = next_node

    return previous
