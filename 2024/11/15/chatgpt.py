from pprint import pprint
import random

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # def __repr__(self):
    #     # This format makes it clearer when printing nodes in the tree
    #     return f'{self.value} |L:{self.left} |R:{self.right}' if self.value is not None else '-'


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
    n = len(arr)
    if n == 0: 
        return None

    # Create all nodes first
    node_arr = [TreeNode(value) for value in arr]

    # DECLARE root (first node)
    root = node_arr[0]

    def insert_node(node):
        parent, seek = None, root
        is_insert_position_left = True
        while seek is not None:
            parent = seek
            if node.value <= seek.value:
                seek = seek.left
                is_insert_position_left = True
            else:
                seek = seek.right
                is_insert_position_left = False
        
        # Insert the node at the correct position
        if is_insert_position_left:
            parent.left = node
        else:
            parent.right = node

    # Insert the nodes one by one
    for node in node_arr[1:]:
        insert_node(node)

    return root

if __name__ == '__main__':
    arr = list(range(10))
    random.shuffle(arr)

    print(f"Shuffled input: {arr}")

    root = array_to_binary_search_tree(arr)
    print('\n' + '*' * 50)
    print(root)
