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
    yield 'digraph {'
    yield '  fontname="Helvetica,Arial,snas-serif"'
    yield '  node [fontname="Helvetica,Arial,snas-serif"]'
    yield '  edge [fontname="Helvetica,Arial,snas-serif"]'
    yield ''
    yield '  graph [center=1 rankdir=LR]'
    yield ''
    yield '  node [height=0.25 width=0.25 shape="circle" label=""]'
    yield '  node [shape="circle"]'
    yield ''
    yield from [f'  {node.name} [label="{node.label}"]' for node in nodes]
    yield ''
    yield from [f'  {edge.start} -> {edge.end} [label="{edge.label}"]' for edge in edges]
    yield '}'

def arr2list(arr: list[int]):
    n = len(arr)
    if n == 0:
        return None
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

if __name__ == '__main__':
    # arr = [1,3,5,7,9]
    # print(arr2list(arr))
    arrs = [[1,3,5,7,9], [1], [], [2,4,6]]
    for arr in arrs:
        ll = arr2list(arr)
        if ll:
            ll.to_dot()
