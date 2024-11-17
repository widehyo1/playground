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
        while seek is not None:
            if node.value <= seek.value:
                print(f'{seek.value=}, go left')
                parent, seek = seek, seek.left
                is_insert_position_left = True
            else:
                print(f'{seek.value=}, go right')
                parent, seek = seek, seek.right
                is_insert_position_left = False
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

    root = array_to_binary_search_tree(arr)
    print('*' * 200)
    print(root)
