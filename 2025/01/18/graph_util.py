from dataclasses import dataclass
from typing import List, Optional, Any
from pprint import pformat

@dataclass
class DisjoinSet:
    value: Optional[Any] = None
    rank: int = 0
    parent = None

    def __post_init__(self):
        self.parent = self

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        if isinstance(other, DisjoinSet):
            return id(self) == id(other)
        return False

    def __repr__(self):
        # base condition
        if self.parent is self:
            return f'<DS {self.value}({self.rank})*>'
        # biz logic
        return f'<DS {self.value}({self.rank}) -> {self.parent}'

def make_set(value):
    return DisjoinSet(value)

def get_root(ds: DisjoinSet):
    # base condition
    if ds.parent is ds:
        return ds
    # biz logic
    cur_ds = ds
    visited_list = [ds]

    while cur_ds.parent != cur_ds:
        cur_ds = cur_ds.parent
        visited_list.append(cur_ds)

    # path compression
    for target in visited_list:
        target.parent = cur_ds

    return cur_ds

def union(ds_a: DisjoinSet, ds_b: DisjoinSet) -> bool:
    root_a = get_root(ds_a)
    root_b = get_root(ds_b)

    # base condition
    if root_a is root_b:
        return True

    # biz logic
    if root_a.rank > root_b.rank:
        root_b.parent = root_a
    elif root_a.rank < root_b.rank:
        root_a.parent = root_b
    else:
        root_a.parent = root_b
        root_b.rank += 1

    return False

@dataclass
class Node:
    value: Optional[Any] = None

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        # Nodes are equal if they have the same value
        if isinstance(other, Node):
            return self.value == other.value
        return False

@dataclass
class Edge:
    src_node: Node
    dst_node: Node

    def __hash__(self):
        # Combine the hash of both nodes in the directed order (src -> dst)
        return hash((self.src_node, self.dst_node))

    def __eq__(self, other):
        if isinstance(other, Edge):
            # Edges are equal only if both src and dst nodes match (order matters)
            return self.src_node == other.src_node and self.dst_node == other.dst_node
        return False

@dataclass
class Graph:
    nodes: Optional[List[Node]] = None
    edges: Optional[List[Edge]] = None

    def __post_init__(self):
        self.nodes = self.nodes or []
        self.edges = self.edges or []

    def is_valid(self):
        nodes = self.nodes
        nodes_set = set(nodes)
        edges = self.edges

        for edge in edges:
            src_node, dst_node = edge.src_node, edge.dst_node
            if src_node not in nodes_set:
                return False
            if dst_node not in nodes_set:
                return False

        return True

    @classmethod
    def from_adjacent_list(cls, adj_list: dict):

        def _gen_nodes(lst):
            for value in lst:
                yield Node(value)

        def _gen_edges(items):
            for item in items:
                src_node_value, dst_node_values = item
                for dst_node_value in dst_node_values:
                    yield Edge(Node(src_node_value), Node(dst_node_value))

        nodes = list(_gen_nodes(adj_list.keys()))
        edges = list(_gen_edges(adj_list.items()))

        g = Graph(nodes, edges)
        if g.is_valid():
            return g
        else:
            return None

    def is_cyclic(self):
        assert self.is_valid(), 'invalid graph'

        ds_inventory = {node.value: make_set(node) for node in self.nodes}

        for edge in self.edges:
            src_node, dst_node = edge.src_node, edge.dst_node
            result = union(ds_inventory[src_node.value], ds_inventory[dst_node.value])
            if result:
                return result
        return False

    def is_connected(self):
        assert self.is_valid(), 'invalid graph'
        assert len(self.nodes) > 0, 'empty graph'

        ds_inventory = {node.value: make_set(node) for node in self.nodes}

        for edge in self.edges:
            src_node, dst_node = edge.src_node, edge.dst_node
            union(ds_inventory[src_node.value], ds_inventory[dst_node.value])

        # Get the root of the first node
        first_root = get_root(ds_inventory[self.nodes[0].value])

        # Check if all nodes have the same root as the first node
        for ds in ds_inventory.values():
            if get_root(ds) != first_root:
                return False  # If any node doesn't have the same root, the graph is not connected

        return True

    def get_undirectional_graph(self):
        edges_set = set(self.edges)
        full_edges = self.edges[::]
        for edge in self.edges:
            src_node, dst_node = edge.src_node, edge.dst_node
            rev_edge = Edge(dst_node, src_node)
            if rev_edge not in edges_set:
                full_edges.append(rev_edge)

        return Graph(self.edges, full_edges)

    def is_tree(self):
        assert self.is_valid(), 'invalid graph'
        assert len(self.nodes) > 0, 'empty graph'

        g = self.get_undirectional_graph()
        return g.is_connected() and not g.is_cyclic()

    def get_adjacent_list(self):
        adj_list = {node.value: [] for node in self.nodes}
        for edge in self.edges:
            src_node, dst_node = edge.src_node, edge.dst_node
            src_val, dst_val = src_node.value, dst_node.value
            adj_list[src_val].append(dst_val)
        return adj_list

    def __repr__(self):
        assert self.is_valid(), 'invalid graph'
        return f'<Graph: \n{pformat(self.get_adjacent_list())}\n>'

Graph.EMPTY = Graph()

if __name__ == '__main__':
    adj_list = {
        1: [2, 3, 4],
        2: [3, 4],
        3: [4],
        4: []
    }
    g = Graph.from_adjacent_list(adj_list)
    print(g)

    print(Graph.EMPTY)

