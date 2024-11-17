class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def del_node(root, key):
    if not root:
        return None

    # Helper function to find the node and its parent
    def find_node_and_parent(root, key):
        parent, current = None, root
        while current:
            if current.val == key:
                return parent, current
            parent = current
            if key < current.val:
                current = current.left
            else:
                current = current.right
        return None, None  # Node not found

    # Helper function to find the in-order successor and its parent
    def find_successor(node):
        current = node.right
        parent = node
        while current and current.left:
            parent = current
            current = current.left
        return parent, current

    # Case 1: Node to be deleted has no left child (can be replaced by right child)
    def delete_with_one_or_no_child(parent, node):
        if parent is None:
            # If the node is the root and has no left child
            return node.right
        if parent.left == node:
            parent.left = node.right
        else:
            parent.right = node.right
        return root

    # Case 2: Node to be deleted has no right child (can be replaced by left child)
    def delete_with_left_child(parent, node):
        if parent is None:
            return node.left
        if parent.left == node:
            parent.left = node.left
        else:
            parent.right = node.left
        return root

    # Case 3: Node to be deleted has two children
    def delete_with_two_children(parent, node):
        # Find the successor
        successor_parent, successor = find_successor(node)
        node.val = successor.val  # Replace value with successor's value
        # Remove successor node
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
        return root

    # Find the node and its parent
    parent, node = find_node_and_parent(root, key)

    if not node:
        return root  # Node not found, return the original root

    # Deletion cases
    if node.left is None and node.right is None:
        if parent is None:
            return None  # Root node with no children, return None
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    elif node.left is None:
        return delete_with_one_or_no_child(parent, node)
    elif node.right is None:
        return delete_with_left_child(parent, node)
    else:
        return delete_with_two_children(parent, node)

    return root
