from tasks.data_structures.double_connected_node.solution import (
    DoubleConnectedNode,
    solution,
)


def test_single_node() -> None:
    node = DoubleConnectedNode(1)
    new_head = solution(node)

    assert new_head is node
    assert new_head.next is None
    assert new_head.prev is None


def test_two_nodes() -> None:
    a = DoubleConnectedNode("first")
    b = DoubleConnectedNode("second")
    a.next = b
    b.prev = a

    new_head = solution(a)

    assert new_head is b
    assert new_head.value == "second"
    assert new_head.next is a
    assert new_head.prev is None
    assert a.next is None
    assert a.prev is b


def test_three_nodes() -> None:
    nodes = [DoubleConnectedNode(i) for i in range(3)]
    for i in range(2):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    new_head = solution(nodes[0])

    assert new_head is nodes[2]
    assert new_head.next is nodes[1]
    assert nodes[1].next is nodes[0]
    assert nodes[0].next is None
    assert nodes[0].prev is nodes[1]
    assert nodes[1].prev is nodes[2]
    assert nodes[2].prev is None


def test_five_nodes_full_check() -> None:
    values = ["A", "B", "C", "D", "E"]
    nodes = [DoubleConnectedNode(v) for v in values]
    for i in range(4):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    new_head = solution(nodes[0])

    assert new_head is nodes[4]
    assert new_head.value == "E"
    assert new_head.prev is None

    expected_order = ["E", "D", "C", "B", "A"]
    cur: DoubleConnectedNode | None = new_head
    for val in expected_order:
        assert cur is not None
        assert cur.value == val
        if cur.next:
            assert cur.next.prev is cur
        cur = cur.next

    assert cur is None


def test_original_example() -> None:
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1
    node1.prev = node0

    node1.next = node2
    node2.prev = node1

    node2.next = node3
    node3.prev = node2

    new_head = solution(node0)

    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node1.next is node0
    assert node0.next is None

    assert node3.prev is None
    assert node2.prev is node3
    assert node1.prev is node2
    assert node0.prev is node1


def test_large_list() -> None:
    n = 1000
    nodes = [DoubleConnectedNode(i) for i in range(n)]
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]

    new_head = solution(nodes[0])

    assert new_head is nodes[-1]
    assert new_head.value == n - 1
    assert new_head.prev is None

    cur: DoubleConnectedNode | None = new_head
    for i in range(n - 1, -1, -1):
        assert cur is not None
        assert cur.value == i
        cur = cur.next

    assert cur is None
