import os
from pathlib import Path
from collections import deque
from pprint import pprint

class TreeNode:
    def __init__(self, value=None, children=None, parent=None):
        self.value = value
        self.children = children
        self.parent = parent

    def __repr__(self):
        if not self.children:
            return f'{self.value}*'
        return f'{self.value}|children:{[child.value for child in self.children]}'
        # return f'{self.value}|children:{[child for child in self.children]}'

def gen_walk_without_hidden(path: str):
    for root, dirs, files in os.walk(path):
        current_part = Path(root).parts
        if sum(1 for part in current_part if part.startswith('.')):
            continue

        dirs = [_dir for _dir in dirs if not _dir.startswith('.')]
        files = [_file for _file in files if not _file.startswith('.')]
        yield root, dirs, files

def walker_to_file_system_tree(walker):
    _counter = 0
    _inventory = {}
    for root, dirs, files in walker:
        if _counter == 0:
            # make root node
            root_node = TreeNode(root, [])
            _inventory[root] = root_node
        for _dir in dirs:
            key = f'{root}{os.sep}{_dir}'
            # create node with parent node
            dir_node = TreeNode(key, [], _inventory[root])
            # register to inventory
            _inventory[key] = dir_node
            # append children
            _inventory[root].children.append(dir_node)
        for _file in files:
            key = f'{root}{os.sep}{_file}'
            # create node
            file_node = TreeNode(key, None, _inventory[root])
            # register to inventory
            _inventory[key] = file_node
            # append children
            _inventory[root].children.append(file_node)
        _counter += 1
    return root_node

def serialize_tree_structure(root: TreeNode) -> dict:
    """
    walk through tree with bfs manner and make node id whenever
    meet a node
    """
    node_id, parent_id, node = 0, None, root
    queue = deque()
    walker = 0
    queue.append((node_id, parent_id, node))
    tree_structure_repr = {}
    while queue:
        node_id, parent_id, node = queue.popleft()
        # print(node_id, parent_id, node)
        if node.children:
            parent_id = node_id
            tree_structure_repr[parent_id] = []
            for child in node.children:
                walker += 1
                tree_structure_repr[parent_id].append(walker)
                queue.append((walker, parent_id, child))
    return tree_structure_repr

def structure_to_gap_repr(tree_structure_repr):
    return {k: gap_repr(v) for k, v in tree_structure_repr.items()}

def gap_repr(array):
    gapped_array = [array[0]]
    for cur, nxt in zip(array, array[1:]):
        gapped_array.append(nxt - cur)
    return gapped_array

def compress_by_value(array):
    from itertools import groupby
    return [array[0]] + [(grouper, sum(1 for _ in it)) for grouper, it in groupby(array[1:])]

def gap_to_compressed_repr(gap_repr):
    return {k: compress_by_value(v) for k, v in gap_repr.items()}

def compressed_to_gap_repr(compressd_repr):
    gapped_repr = {}
    for key, value in compressd_repr.items():
        head, *tail = value
        arr = [head]
        for num, count in tail:
            arr += [num] * count
        gapped_repr[key] = arr
    return gapped_repr

def gap_to_structured_repr(gapped_repr):
    tree_structure_repr = {}
    for key, value in gapped_repr.items():
        head, *tail = value
        cur = head
        value = [cur]
        for gap in tail:
            cur = cur + gap
            value.append(cur)
        tree_structure_repr[key] = value
    return tree_structure_repr


def deserialize_tree_structure(tree_structure_repr: dict):
    # pprint(tree_structure_repr)
    _inventory = {}
    root_node = None
    for key, value in tree_structure_repr.items():
        _inventory[key] = TreeNode(key)
        if not root_node:
            root_node = _inventory[key]
        for node_id in value:
            _inventory[node_id] = TreeNode(node_id)

    for key, value in tree_structure_repr.items():
        _inventory[key].children = [_inventory[node_id] for node_id in value]
        for node_id in value:
            _inventory[node_id].parent = _inventory[key]

    return root_node


if __name__ == '__main__':
    path = '.'
    file_system_tree = walker_to_file_system_tree(gen_walk_without_hidden(path))
    tree_structure_repr = serialize_tree_structure(file_system_tree)
    # print('=== tree structure representation ===')
    # pprint(tree_structure_repr)
    # print()
    gapped_repr = structure_to_gap_repr(tree_structure_repr)
    # print('=== gapped representation ===')
    # pprint(gapped_repr)
    # print()
    compressd_repr = gap_to_compressed_repr(gapped_repr)
    print('=== compressed representation ===')
    pprint(compressd_repr)
    print()
    _gapped_repr = compressed_to_gap_repr(compressd_repr)
    # print('=== _gapped representation ===')
    # pprint(_gapped_repr)
    # print()
    _tree_structure_repr = gap_to_structured_repr(_gapped_repr)
    # print('=== _tree structure representation ===')
    # pprint(_tree_structure_repr)
    # print()
    tree_root = deserialize_tree_structure(_tree_structure_repr)
    # pprint(tree_root)


