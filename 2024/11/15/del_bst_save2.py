from pprint import pprint, pformat
import random

bk = breakpoint

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
    node_arr = [TreeNode(value) if value is not None else None for value in arr]
    # DECLARE free variable: root
    root = node_arr[0]
    def insert_node(node):
        if node is None:
            return
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

def del_node(root, key):
    # base condition
    if root is None: return None

    # DECLARE free variable: root
    def seek(key):
        """
        return is a tuple consists of:
        is_found: True or False

        if is_found is False: return False, None, None, None
        else:

        node: found node with value is equal to key
        parent: parent node of the node
        is_left: position of the node with respect to parent, True or False
        """
        is_found = False
        is_left = None
        parent, curnode = None, root
        while curnode:
            if key < curnode.value:
                parent, curnode = curnode, curnode.left
                is_left = True
            elif key > curnode.value:
                parent, curnode = curnode, curnode.right
                is_left = False
            else:
                is_found = True
                return is_found, curnode, parent, is_left
        return is_found, None, None, None

    # biz logic
    # is_found, target, parent, is_left = seek(key)
    is_found, target, target_parent, is_left = seek(key)
    if not is_found:
        return root

    successor, successor_parent = find_successor(target)

    # when deleting node(target) is the root
    if target_parent is None:
        if target.left is None:
            root = root.right
        elif target.right is None:
            root = root.left
        else:
            # find successor's parent and unlink
            target.value = successor.value
            # delete successor gracefully
            if successor_parent is target:
                # succesor lies on right side with respect to successor_parent
                target.right = successor.right
            else:
                successor_parent.left = None
        return root

    if target.left is None:
        if is_left:
            target_parent.left = target.right
        else:
            target_parent.right = target.right
    elif target.right is None:
        if is_left:
            target_parent.left = target.left
        else:
            target_parent.right = target.left
    else:
        # swap target and successor
        target.value = successor.value
        # delete successor gracefully
        if successor_parent is target:
            # succesor lies on right side with respect to successor_parent
            target.right = successor.right
        else:
            successor_parent.left = None
    return root


    # return root

def find_successor(node: TreeNode):
    """
    return is a tuple consists of:
    successor: founded successor of the node
    successor_parent: parent node of the successor, or None if successor is node
    is_left can be checked by successor_parent is None or not
    """
    if node.right is None:
        return node, None

    successor_parent, successor, curnode = None, node, node.right
    while curnode:
        successor_parent = successor
        successor = curnode
        curnode = curnode.left
    return successor, successor_parent



if __name__ == '__main__':
    # arr = list(range(70))
    # arr = list(range(16))
    # arr = list(range(8))
    # arr = [5,3,6,2,4,None,7]
    # arr = [0]
    arr = [2,0,33,None,1,25,40,None,None,11,31,34,45,10,18,29,32,None,36,43,46,4,None,12,24,26,30,None,None,35,39,42,44,None,48,3,9,None,14,22,None,None,27,None,None,None,None,38,None,41,None,None,None,47,49,None,None,5,None,13,15,21,23,None,28,37,None,None,None,None,None,None,None,None,8,None,None,None,17,19,None,None,None,None,None,None,None,7,None,16,None,None,20,6]

    root = array_to_binary_search_tree(arr)
    print('*' * 200)
    print(root)

    key = 33
    print(f'{key=}')

    result = del_node(root, key)

    print(f'{result=}')
