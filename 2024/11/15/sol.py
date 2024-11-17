from pprint import pprint, pformat
import random

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self, level=0):
        # Base case: if the node is None, return an empty string
        if self is None:
            return "None"

        # Prepare the prefix for indentation based on the level
        indent = "   " * level
        result = f"{indent}{self.value}\n"

        # Recursively represent the left and right children
        if self.left or self.right:
            if self.left:
                result += f"{indent}L-> " + (self.left.__repr__(level + 1) if self.left else "None\n")
            else:
                result += f"{indent}L-> None\n"
            if self.right:
                result += f"{indent}R-> " + (self.right.__repr__(level + 1) if self.right else "None\n")
            else:
                result += f"{indent}R-> None\n"

        return result

def array_to_binary_search_tree(arr):
    pprint(f'given {arr=}')
    n = len(arr)
    # base condition
    if n == 0: return None
    # construct TreeNode
    node_arr = [TreeNode(value) for value in arr]
    # DECLARE free variable: root
    root = node_arr[0]
    def insert_node(node):
        parent, seek = None, root
        is_insert_position_left = True
        while seek is not None:
            if node.value <= seek.value:
                parent, seek = seek, seek.left
                is_insert_position_left = True
            else:
                parent, seek = seek, seek.right
                is_insert_position_left = False
        if is_insert_position_left:
            parent.left = node
        else:
            parent.right = node

    for node in node_arr[1:]:
        insert_node(node)
    return root

if __name__ == '__main__':
    arr = list(range(10))

    random.shuffle(arr)

    root = array_to_binary_search_tree(arr)
    print('*' * 200)
    print(root)
