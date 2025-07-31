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
    yield from [
        f'  {edge.start} -> {edge.end} [label="{edge.label}"]' for edge in edges
    ]
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


def remove_duplicate(llist: LinkedList) -> LinkedList:
    head = llist.head
    if head is None:
        return llist
    cur_node = head.next
    if cur_node is None:
        return llist
    distinct_value_set = set()
    distinct_value_set.add(head.val)
    prev_node = head
    while cur_node:
        if cur_node.val in distinct_value_set:
            cur_node = cur_node.next
        else:
            distinct_value_set.add(cur_node.val)
            prev_node.next = cur_node
            cur_node, prev_node = cur_node.next, cur_node
    prev_node.next = None
    return LinkedList(head)

def last_kth_element(llist: LinkedList, k: int) -> int:
    print(llist)
    head = llist.head
    if head is None:
        return None
    fst = head
    for _ in range(k - 1):
        if fst is None:
            return None
        fst = fst.next
    snd = head
    while fst.next is not None:
        fst = fst.next
        snd = snd.next
    # fst.next is None, thus, fst is the last element
    return snd.val, snd


def add_group(cur, walker, grp_head):
    if walker is None:
        grp_head = cur
    else:
        walker.next = cur
    walker = cur
    return walker, grp_head


def partition(llist: LinkedList, x):
    fst = None
    fst_head = None
    snd = None
    snd_head = None

    head = llist.head
    if head is None:
        return llist

    cur = head

    # move current node to last element
    while cur.next is not None:
        cur_val = cur.val
        if cur.val > x:
            snd, snd_head = add_group(cur, snd, snd_head)
        else:
            fst, fst_head = add_group(cur, fst, fst_head)
        cur = cur.next
    if cur.val > x:
        snd, snd_head = add_group(cur, snd, snd_head)
    else:
        fst, fst_head = add_group(cur, fst, fst_head)

    if snd_head is None:
        return llist

    if fst_head is None:
        return llist

    snd.next = None
    fst.next = snd_head
    return LinkedList(fst_head)

def add_two_number(llist1, llist2):
    carry = 0
    fst_node, snd_node = llist1.head, llist2.head

    head = ListNode(None)
    curnode = head

    while fst_node or snd_node or carry == 1:
        step_val = 1 if carry else 0
        if fst_node is not None:
            step_val += fst_node.val
            fst_node = fst_node.next
        if snd_node is not None:
            step_val += snd_node.val
            snd_node = snd_node.next
        carry, step_val = divmod(step_val, 10)
        newnode = ListNode(step_val)
        curnode.next = newnode
        curnode = newnode

    return LinkedList(head.next)

def reverse(llist):
    head = llist.head
    if head is None:
        return llilst
    if head.next is None:
        return llist
    prevnode = None
    curnode = head
    newhead = None
    while curnode.next:
        temp = prevnode
        curnode, prevnode = curnode.next, curnode
        prevnode.next = temp
        print(prevnode)
    curnode.next = prevnode
    return LinkedList(curnode)



if __name__ == "__main__":
    # arr = [1,3,5,7,9]
    # print(arr2list(arr))
    # arrs = [[1, 3, 5, 7, 9], [1], [], [2, 4, 6]]
    # arrs = [[1, 1, 1], [1], [], [2, 3, 1, 2, 2, 3, 6, 1]]
    # for arr in arrs:
    #     llist = arr2list(arr)
    #     # res = remove_duplicate(llist)
    #     # res.to_dot()
    #     # res = last_kth_element(llist, 3)
    #     # if res is not None:
    #     #     print(res)
    #     # else:
    #     #     print("invalid input")
    #     res = partition(llist, 2)
    #     res.to_dot()
    arr1, arr2 = [7,1,6], [5,9,2]
    # arr1, arr2 = [1,1,3], [9,9,9,9,9]
    llist1, llist2 = arr2list(arr1), arr2list(arr2)
    res = add_two_number(llist1, llist2)

    print(res)
    print("--")
    llist1, llist2 = arr2list(arr1), arr2list(arr2)
    res2 = reverse(add_two_number(reverse(llist1), reverse(llist2)))
    print(reverse(llist1))
    print(reverse(llist2))
    print(add_two_number(reverse(llist1), reverse(llist2)))
    print(res2)
