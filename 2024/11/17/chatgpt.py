class Node:
    def __init__(self, key=None, child=None, nxt=None, is_word=False):
        self.key = key
        self.child = child
        self.nxt = nxt
        self.is_word = is_word

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        if not word:
            return

        curnode = self.head
        for char in word:
            # Traverse the current children to find the appropriate node or add one
            curnode = self._find_or_add_child(curnode, char)
        curnode.is_word = True

    def search(self, word: str) -> bool:
        curnode = self.head
        for char in word:
            curnode = self._find_child(curnode, char)
            if curnode is None:
                return False
        return curnode.is_word

    def startsWith(self, prefix: str) -> bool:
        curnode = self.head
        for char in prefix:
            curnode = self._find_child(curnode, char)
            if curnode is None:
                return False
        return True

    def _find_or_add_child(self, parent: Node, key: str) -> Node:
        """Helper to find or add a child node with the given key."""
        if not parent.child:
            parent.child = Node(key)
            return parent.child
        
        # Check if key is already in the siblings chain
        sibling = self._find_key_in_sibling_or_none(parent.child, key)
        if sibling:
            return sibling
        
        # If not found, append as a new sibling at the end
        last_sibling = self._get_last_sibling(parent.child)
        return self._append_sibling(last_sibling, key)

    def _find_child(self, parent: Node, key: str) -> Node:
        """Helper to find a child node by its key."""
        return self._find_key_in_sibling_or_none(parent.child, key)

    def _find_key_in_sibling_or_none(self, node: Node, key: str) -> Node:
        """Search for a node with the given key among siblings."""
        while node:
            if node.key == key:
                return node
            node = node.nxt
        return None

    def _get_last_sibling(self, node: Node) -> Node:
        """Find the last sibling in the chain."""
        while node and node.nxt:
            node = node.nxt
        return node

    def _append_sibling(self, node: Node, key: str) -> Node:
        """Append a sibling node with the given key."""
        new_node = Node(key)
        node.nxt = new_node
        return new_node


# Example usage:
if __name__ == '__main__':
    trie = Trie()
    words = ["A", "in", "i", "inn", "to", "tea", "ted"]
    for word in words:
        trie.insert(word)

    print('*' * 200)
    search_words = ["B", "A", "i", "t", "in", "inn", "iinn", "innn", "to", "tea", "ted", "todd"]
    for search_word in search_words:
        print(f"search({search_word}): {trie.search(search_word)}")

    print('*' * 200)
    for search_word in search_words:
        print(f"startsWith({search_word}): {trie.startsWith(search_word)}")

    print('*' * 200)
