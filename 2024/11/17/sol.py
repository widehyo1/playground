from pprint import pprint, pformat

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            node = node.get(char, None)
            if not node:
                return False
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            node = node.get(char, None)
            if not node:
                return False
        return True

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

    pprint(trie.root)

    print('*' * 200)
    search_words = ["B", "A", "i", "t", "in", "inn", "iinn", "innn", "to", "tea", "ted", "todd"]
    for search_word in search_words:
        trie.search(search_word)

    print('*' * 200)
    for search_word in search_words:
        trie.startsWith(search_word)

    print('*' * 200)
