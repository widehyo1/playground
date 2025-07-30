from typing import Optional, NamedTuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"{self.val}"
        else:
            return f"{self.val} -> {self.next}"


class Node(NamedTuple):
    name: str
    label: str


class Edge(NamedTuple):
    start: str
    end: str
    label: str


class Graph(NamedTuple):
    nodes: list[Node]
    edges: list[Edge]


def nodename(id_: int) -> str:
    return f"n{id_}"


def to_node(id_: int, label: str = None) -> Node:
    if label is None:
        label = nodename(id_)
    return Node(nodename(id_), label)


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    def __repr__(self):
        return f"< LinkedList: {self.head} >"

    def extract_graph(self) -> Graph:
        if self.head is None:
            return None
        nodes = []
        edges = []
        node_cnt = 0

        cur_node = self.head
        # process head
        nodes.append(to_node(node_cnt, f"{cur_node.val}"))

        while cur_node.next is not None:
            node_cnt += 1
            cur_node, prev_node = cur_node.next, cur_node
            nodes.append(to_node(node_cnt, f"{cur_node.val}"))
            edges.append(Edge(nodename(node_cnt - 1), nodename(node_cnt), ""))

        # cur_node is tail node
        return Graph(nodes, edges)

    def to_dot(self):
        graph = self.extract_graph()
        if graph is None:
            print("linked list is empty")
            return
        print("\n".join(graph_to_dot(graph)))


def graph_to_dot(graph: Graph):
    nodes, edges = graph
    yield "digraph {"
    yield '  fontname="Helvetica,Arial,snas-serif"'
    yield '  node [fontname="Helvetica,Arial,snas-serif"]'
    yield '  edge [fontname="Helvetica,Arial,snas-serif"]'
    yield ""
    yield "  graph [center=1 rankdir=LR]"
    yield ""
    yield '  node [height=0.25 width=0.25 shape="circle" label=""]'
    yield '  node [shape="circle"]'
    yield ""
    yield from [f'  {node.name} [label="{node.label}"]' for node in nodes]
    yield ""
    yield from [f'  {edge.start} -> {edge.end} [label="{edge.label}"]' for edge in edges]
    yield "}"


def arr2list(arr: list[int]):
    n = len(arr)
    if n == 0:
        return LinkedList(None)
    head_node = ListNode(arr[0])
    linked_list = LinkedList(head_node)
    if n == 1:
        return linked_list

    idx = 1
    cur_node = head_node

    while idx < n:
        cur_node, prev_node = ListNode(arr[idx]), cur_node
        prev_node.next = cur_node
        idx += 1

    return linked_list


def reverseNode(node):
    # base case
    if node is None:
        return node

    head = node
    if head.next is None:
        return head

    # base case2: only two node
    if head.next.next is None:
        next = head.next
        head.next = None
        next.next = head
        return next

    # biz logic1: process head node
    cur = head.next
    prev = head
    head.next = None

    # biz logic2: loop
    while cur.next:
        temp = prev
        prev = cur
        cur = cur.next
        prev.next = temp

    # biz logic3: post last node
    cur.next = prev

    return cur

def reverse(llist):
    headnode = llist.head
    llist.head = reverseNode(headnode)
    return llist

def add_two_number(lst1, lst2):
    # init phase
    carry = 0
    node1, node2 = lst1.head, lst2.head
    prev_head = ListNode(None)
    prev = prev_head

    while node1 is not None or node2 is not None or carry == 1:
        stepval = 0
        if node1:
            stepval += node1.val
            node1 = node1.next
        if node2:
            stepval += node2.val
            node2 = node2.next
        if carry:
            stepval += 1
        carry, stepval = divmod(stepval, 10)
        node = ListNode(stepval)
        prev.next = node
        prev = node

    node = prev_head.next
    return LinkedList(node)

def add_two_number_rev(lst1, lst2):
    return reverse(add_two_number(reverse(lst1), reverse(lst2)))

# if __name__ == "__main__":
#     # arr = [1,3,5,7,9]
#     # print(arr2list(arr))
#     arrs = [[1, 3, 5, 7, 9], [1], [], [2, 4, 6]]
#     for arr in arrs:
#         ll = arr2list(arr)
#         # print(ll)
#         if ll:
#             ll.to_dot()
#             reverse(ll).to_dot()

if __name__ == "__main__":
    # arr = [1,3,5,7,9]
    # print(arr2list(arr))
    arrs1 = [[1, 3, 5, 7, 9], [], [], [9,9,9,1]]
    arrs2 = [[5, 7, 9], [1, 2], [], [1]]
    for arr1, arr2 in zip(arrs1, arrs2):
        ll1, ll2 = arr2list(arr1), arr2list(arr2)
        print(ll1)
        print(ll2)
        print("===")
        print(add_two_number(ll1, ll2))
        print("###")

    print("reverse phase")
    for arr1, arr2 in zip(arrs1[::-1], arrs2[::-1]):
        ll1, ll2 = arr2list(arr1), arr2list(arr2)
        print(ll1)
        print(ll2)
        print("===")
        print(add_two_number_rev(ll1, ll2))
        print("###")
