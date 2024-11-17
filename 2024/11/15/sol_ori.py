from pprint import pprint, pformat
import random

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        r_value = self.value if self.value is not None else '-'
        r_left = self.left if self.left is not None else '-'
        r_right = self.right if self.right is not None else '-'
        if r_left == '-' and r_right == '-':
            return f'{r_value}*'
        return f'{r_value}|L:{self.left}|R:{self.right}'

def array_to_tree(arr):
    n = len(arr)
    # base condition
    if n == 0: return None
    # DECLARE free variable: n
    def has_left_child(idx):
        return 2 * idx + 1 < n
    def has_right_child(idx):
        return 2 * idx + 2 < n
    # construct TreeNode
    node_arr = [TreeNode(value) for value in arr]
    for idx, node in enumerate(node_arr):
        if idx == 0: root = node
        if has_left_child(idx):
            node.left = node_arr[2*idx + 1]
        if has_right_child(idx):
            node.right = node_arr[2*idx + 2]
    return root

def array_to_binary_search_tree(arr):
    n = len(arr)
    # base condition
    if n == 0: return None
    # construct TreeNode
    node_arr = [TreeNode(value) for value in arr]
    pprint(f'{node_arr=}')
    # DECLARE free variable: root
    root = node_arr[0]
    def insert_node(node):
        print(f'insert_node({node})')
        parent, seek = None, root
        is_insert_position_left = True
        stack = [(parent, seek, is_insert_position_left)]
        while stack:
            pprint(f'{stack=}')
            parent, seek, is_insert_position_left = stack.pop()
            if seek is None:
                print(f'found position, break')
                print(f'{parent=}, {is_insert_position_left=}')
                break
            if node.value <= seek.value:
                print(f'{seek.value=}, go left')
                stack.append((seek, seek.left, True))
            else:
                print(f'{seek.value=}, go right')
                stack.append((seek, seek.right, False))
        if is_insert_position_left:
            print('append node to left child')
            parent.left = node
        else:
            print('append node to rigth child')
            parent.right = node

        print(f'{root=}')
        print('=' * 100)

    for node in node_arr[1:]:
        pprint(f'{root=}')
        pprint(f'{node=}')
        insert_node(node)
    return root

if __name__ == '__main__':
    arr = list(range(10))

    random.shuffle(arr)

    # root = array_to_tree(arr)
    # print(root)

    # root = array_to_binary_search_tree(arr)
    # print('*' * 200)
    # print(root)

    # root = array_to_binary_search_tree(list(reversed(arr)))
    # print('*' * 200)
    # print(root)

    root = array_to_binary_search_tree(arr)
    print('*' * 200)
    print(root)
