import os
from pathlib import Path
from collections import deque

class TreeNode:
    def __init__(self, value=None, children=None, parent=None):
        self.value = value
        self.children = children
        self.parent = parent

    def __repr__(self):
        if not self.children:
            return f'{self.value}*'
        return f'{self.value}|children:{[child.value for child in self.children]}'

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

def serialize_tree_depth_structure(root: TreeNode) -> dict:
    """
    walk through tree with bfs manner and make node id whenever
    meet a node
    """
    node_id, node = 0, root
    walker = 0
    queue = deque()
    queue.append((node_id, node))
    result = {}
    while queue:
        node_id, node = queue.popleft()
        if node.children:
            node_id += 1
            if not result.get(node_id, None):
                result[node_id] = []
            for child in node.children:
                walker += 1
                result[node_id].append(walker)
                queue.append((node_id, child))
    return result

if __name__ == '__main__':
    path = '.'
    file_system_tree = walker_to_file_system_tree(gen_walk_without_hidden(path))
    tree_structure = serialize_tree_depth_structure(file_system_tree)
    print(tree_structure)

