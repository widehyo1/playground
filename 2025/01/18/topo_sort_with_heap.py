import heapq
from graph_util import Graph
from itertools import groupby

class Node:
    def __init__(self, value, execution_time):
        self.value = value
        self.execution_time = execution_time  # New property to represent the execution time

    def __lt__(self, other):
        # Invert the comparison to create a max-heap based on execution time
        return self.execution_time > other.execution_time

    def __repr__(self):
        return f"Node({self.value}, {self.execution_time})"


def topological_sort_with_priority(g: Graph):
    assert not g.is_cycle(), 'Graph is not acyclic'  # Ensure the graph is a DAG

    # Initialize in-degree counter (number of incoming edges for each node)
    node_counter = {node.value: 0 for node in g.nodes}
    
    for edge in g.edges:
        dst_node = edge.dst_node
        dst_value = dst_node.value
        node_counter[dst_value] += 1

    # Group edges by source node value for easy traversal
    get_src_value = lambda edge: edge.src_node.value
    src_sorted_edges = sorted(g.edges, key=get_src_value)
    edge_group = {
        key: list(g_group)
        for key, g_group in groupby(src_sorted_edges, key=get_src_value)
    }

    # Business logic: Start with nodes having no incoming edges (in-degree == 0)
    available_nodes = [node for node in g.nodes if node_counter[node.value] == 0]

    # Convert the available nodes into a max-heap based on execution time
    heapq.heapify(available_nodes)  # Heapify the list in O(n) time

    topo_sort_order = []

    while available_nodes:
        node = heapq.heappop(available_nodes)  # Get the node with the highest execution time
        topo_sort_order.append(node.value)

        # Process edges originating from the current node
        for edge in edge_group[node.value]:
            dst_node = edge.dst_node
            dst_value = dst_node.value

            # Reduce the in-degree of destination node
            node_counter[dst_value] -= 1

            # If the destination node has no more incoming edges, add it to the heap
            if node_counter[dst_value] == 0:
                heapq.heappush(available_nodes, dst_node)

    return topo_sort_order
