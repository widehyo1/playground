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

def del_node_from_bst(root, node):
    # base condition
    if root is None: return None

    # DECLARE free variable: root
    # seek node in binary search tree
    def seek(node):
        parent, curnode = None, root
        is_node_at_left = True
        is_found = False
        while curnode:
            if node.value < curnode.value:
                parent, curnode = curnode, curnode.left
                is_node_at_left = True
            elif node.value > curnode.value:
                parent, curnode = curnode, curnode.right
                is_node_at_left = False
            else:
                is_found = True
                return is_found, parent, is_node_at_left
        is_found, parent, is_node_at_left = False, None, None
        return is_found, parent, is_node_at_left

    def get_succesor(node):
        grand_parent, parent, succesor = None, node, node.right
        while succesor:
            grand_parent, parent, succesor = parent, succesor, succesor.left
        return grand_parent, parent

    # biz logic

    if type(node) is not TreeNode:
        # consider node represents TreeNode with value as node
        node = TreeNode(node)

    # i tried to code first like this:
    # "if node is root:" to enhance clearity that i am really comparing node is the same object with root
    # but, in this case, you must send node to parameter to del_node_from_bst which is resides in bst and
    # you must point that node for some way. i.e. target_node = root.left.left.right
    # it burdens and unnessessary on dealing with binary search tree
    # which implies each node is comaprable (for some way in general context).
    # Mathematically speaking, it says that TreeNode structure(class) is totally ordered.
    # i.e. for every pair of TreeNode node1 and node2, there are only three cases:
    # node1 > node2 (node1.__gt__(node2) is True)
    # node1 == node2 (node1.__eq__(node2) is True)
    # node1 < node2 (node1.__lt__(node2) is True)
    # every TreeNode has value, and if there is no ambiguity to designate node between node.value,
    # we just consider node's value as the node with that value.
    # in real situation, what we focus on and matter is the value other than TreeNode itself.
    # (i.e. instance of <class '__main__.TreeNode'> object)
    # so i changed to focus on comparing node.value and root.value and use "==" operator
    # to focus on equality rather than identity, for the purpose of make this code work on
    # more general situation which custum __eq__ is implemented

    # case 1: target node is the root node
    if node.value == root.value:
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            # delete root with two children
            # -> in this case, succesor can not be same with root
            # -> succesor_parent is not None
            # -> problem is happens when succesor_parent is None, i.e. succesor is root
            # otherwise, logic is following
            # find succesor
            # swap and delete
            succesor_parent, succesor = get_succesor(node)
            root.value = succesor.value
            # what situation which make trouble is the succesor and root is identical object
            if succesor_parent is root:
                # this happens only if root's right child has no left child.
                # in this case, you juse copy value and update right link of root to succesor's right
                root.right = succesor.right
            else:
                succesor_parent.left = None
        return root

    # case 2: target node is not the root node
    is_found, parent, is_node_at_left = seek(node)
    if not is_found:
        return root

    if target_node.left is None:
        if is_node_at_left:
            parent.left = target_node.right
        else:
            parent.right = target_node.right
    elif target_node.right is None:
        if is_node_at_left:
            parent.left = target_node.left
        else:
            parent.right = target_node.left
    else:
        # succesor_parent is not None because we just checked
        # target_node has left and right child already
        succesor_parent, succesor = get_succesor(target_node)
        # copy succesor's value to target_node
        target_node.value = succesor.value
        # and unlink succesor
        succesor_parent.left = None
    return root

def del_node(root, key):
    # base condition
    if root is None: return None

    # DECLARE free variable: root
    # seek node in binary search tree
    def seek(key):
        parent, curnode = None, root
        is_node_at_left = True
        is_found = False
        while curnode:
            if key < curnode.val:
                parent, curnode = curnode, curnode.left
                is_node_at_left = True
            elif key > curnode.val:
                parent, curnode = curnode, curnode.right
                is_node_at_left = False
            else:
                is_found = True
                return is_found, curnode, parent, is_node_at_left
        is_found, node, parent, is_node_at_left = False, None, None, None
        return is_found, node, parent, is_node_at_left

    def get_succesor(node):
        grand_parent, parent, succesor = None, node, node.right
        while succesor:
            grand_parent, parent, succesor = parent, succesor, succesor.left
        return grand_parent, parent

    # biz logic

    is_found, target_node, parent, is_node_at_left = seek(key)
    if not is_found:
        return root

    if target_node.left is None:
        if is_node_at_left:
            parent.left = target_node.right
        else:
            parent.right = target_node.right
    elif target_node.right is None:
        if is_node_at_left:
            parent.left = target_node.left
        else:
            parent.right = target_node.left
    else:
        succesor_parent, succesor = get_succesor(target_node)
        target_node.val = succesor.val
        if succesor_parent.right is succesor:
            succesor_parent.right = succesor.right
        else:
            succesor_parent.left = None
    return root

def del_node(root, key):
    # base condition
    if root is None: return None

    # DECLARE free variable: root
    # seek node in binary search tree
    def seek(key):
        parent, curnode = None, root
        is_node_at_left = True
        is_found = False
        while curnode:
            if key < curnode.value:
                parent, curnode = curnode, curnode.left
                is_node_at_left = True
            elif key > curnode.value:
                parent, curnode = curnode, curnode.right
                is_node_at_left = False
            else:
                is_found = True
                return is_found, curnode, parent, is_node_at_left
        is_found, node, parent, is_node_at_left = False, None, None, None
        return is_found, node, parent, is_node_at_left

    def get_succesor(node):
        grand_parent, parent, succesor = None, node, node.right
        while succesor:
            grand_parent, parent, succesor = parent, succesor, succesor.left
        return grand_parent, parent

    # biz logic

    is_found, target_node, parent, is_node_at_left = seek(key)
    if not is_found:
        return root

    if target_node is root:
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            succesor_parent, succesor = get_succesor(target_node)
            target_node.value = succesor.value
            if succesor_parent.right is succesor:
                succesor_parent.right = succesor.right
            else:
                succesor_parent.left = None
        return root

    if target_node.left is None:
        if is_node_at_left:
            parent.left = target_node.right
        else:
            parent.right = target_node.right
    elif target_node.right is None:
        if is_node_at_left:
            parent.left = target_node.left
        else:
            parent.right = target_node.left
    else:
        succesor_parent, succesor = get_succesor(target_node)
        del_node(succesor_parent, succesor.value)
        # target_node.value = succesor.value
        # if succesor_parent.right is succesor:
        #     succesor_parent.right = succesor.right
        # else:
        #     succesor_parent.left = None
    return root


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

    # target = root.left.left.right \
    #     if   root.left and root.left.left and root.left.left.right \
    #     else root.left.left if root.left and root.left.left \
    #     else root.left if root.left \
    #     else root

    # target = root

    # print(f'{target=}')

    # key = 3
    # key = 0
    key = 33
    print(f'{key=}')

    result = del_node(root, key)

    print(f'{result=}')
