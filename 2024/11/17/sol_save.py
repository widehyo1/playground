bk = breakpoint
class Node:
    def __init__(self, key=None, child=None, nxt=None, is_word=False):
        self.key = key
        self.child = child
        self.nxt = nxt
        self.is_word = is_word

    def __repr__(self):
        return f'Node({self.key=}, {self.is_word=})'

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        print(f'=== insert({word}) ===')
        if len(word) == 0:
            return

        curnode = self.head
        print(f'for loop start')
        for char in word:
            print(f'{char=}')
            print(f'{curnode=}')
            pre, curnode = curnode, curnode.child
            if curnode is None:
                print('curnode is None')
                pre.child = Node(char)
                curnode = pre.child
                continue
            sibling_node = find_key_in_sibling_or_none(curnode, char)
            if sibling_node is None:
                print('sibling_node is None')
                last_sibling = append_sibling_node_with_key(
                    get_last_sibling(curnode), char
                )
                curnode = last_sibling
                continue
            print('find sibling_node')
            curnode = sibling_node
        print(f'for loop end')
        curnode.is_word = True
        print(f'{curnode=}')

    def search(self, word: str) -> bool:
        print(f'=== search({word}) ===')
        curnode = self.head
        print(f'for loop start')
        for char in word:
            print(f'{char=}')
            print(f'{curnode=}')
            pre, curnode = curnode, curnode.child
            if curnode is None:
                print(f'False')
                return False
            sibling_node = find_key_in_sibling_or_none(curnode, char)
            if sibling_node is None:
                print(f'False')
                return False
            curnode = sibling_node
        print(f'for loop end')
        print(f'{curnode=}')
        return curnode.is_word

    def startsWith(self, prefix: str) -> bool:
        print(f'=== startsWith({prefix}) ===')
        curnode = self.head
        print(f'for loop start')
        for char in prefix:
            print(f'{char=}')
            print(f'{curnode=}')
            pre, curnode = curnode, curnode.child
            if curnode is None:
                print(f'False')
                return False
            sibling_node = find_key_in_sibling_or_none(curnode, char)
            if sibling_node is None:
                print(f'False')
                return False
            curnode = sibling_node
        print(f'for loop end')
        print(f'{curnode=}')
        return True

def make_child_node_with_key(parent: Node, key: str):
    parent.child = Node(key)
    return parent

def append_sibling_node_with_key(node, key):
    node.nxt = Node(key)
    return node.nxt

def find_key_in_sibling_or_none(node: Node, key):
    """
    walk on node.nxt until find node.key == key
    if node is not found, return None
    """
    if node.key == key:
        return node
    while node.nxt:
        node = node.nxt
        if node.key == key:
            return node
    else:
        return None

def get_last_sibling(node: Node):
    curnode = node
    while curnode.nxt:
        curnode = curnode.nxt
    return curnode

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    words = ["A", "in", "i", "inn", "to", "tea", "ted"]
    for word in words:
        trie.insert(word)

    print('*' * 200)
    search_words = ["B", "A", "i", "t", "in", "inn", "iinn", "innn", "to", "tea", "ted", "todd"]
    for search_word in search_words:
        trie.search(search_word)

    print('*' * 200)
    for search_word in search_words:
        trie.startsWith(search_word)

    print('*' * 200)
