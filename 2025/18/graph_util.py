from dataclasses import dataclass
from typing import List, Optional, Any
from pprint import pformat

@dataclass
class Node:
    value: Optional[Any] = None

    def __hash__(self):
        # Use the value of the node as the hash (or any other unique attribute)
        return hash(self.value)

    def __eq__(self, other):
        # Nodes are equal if they have the same value
        if isinstance(other, Node):
            return self.value == other.value
        return False

@dataclass
class Edge:
    src: Node
    dst: Node

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
            src, dst = edge.src, edge.dst
            if src not in nodes_set:
                return False
            if dst not in nodes_set:
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

    def __repr__(self):
        assert self.is_valid(), 'invalid graph'
        # adjacent list version representation
        adj_list = {node.value: [] for node in self.nodes}
        for edge in self.edges:
            src_val, dst_val = edge.src.value, edge.dst.value
            adj_list[src_val].append(dst_val)
        return f'<Graph: \n{pformat(adj_list)}\n>'

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

