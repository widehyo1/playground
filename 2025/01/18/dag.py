from graph_util import Graph
from itertools import groupby

def topological_sort(g: Graph):
    assert not g.is_cycle(), 'graph is not acyclic'

    # initalize
    node_counter = {node.value: 0 for node in g.nodes}
    for edge in g.edges:
        dst_node = edge.dst_node
        dst_value = dst_node.value
        node_counter[dst_value] += 1

    get_src_value = lambda edge: edge.src_node.value
    src_sorted_edges = sorted(g.edges, key=get_src_value)
    edge_group = {
        key: list(g_group)
        for key, g_group in groupby(src_sorted_edges, key=get_src_value)
    }

    # biz logic
    stack = [val for val, cnt in node_counter.items() if cnt == 0] # avaliable_nodes
    topo_sort_order = []

    while stack:
        val = stack.pop()
        topo_sort_order.append(val)
        # edges with source node's value is val
        for edge in edge_group[val]:

            dst_node = edge.dst_node
            dst_value = dst_node.value

            node_counter[dst_value] -= 1
            if node_counter[dst_value] == 0:
                stack.append(dst_value)

    return topo_sort_order



if __name__ == '__main__':
    adj_list = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'D': ['H'],
        'E': ['H'],
        'F': ['H'],
        'G': [],
        'H': []
    }
    g = Graph.from_adjacent_list(adj_list)
    nodes = topological_sort(g)
