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
        print(f'=== search({word}) ===')
        node = self.root
        print('for loop start')
        for char in word:
            print(f'{node=}')
            node = node.get(char, None)
            if not node:
                print('False')
                return False
        # return node.get('#', False)
        print('for loop end')
        print(f'{node=}')
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        print(f'=== startsWith({prefix}) ===')
        node = self.root
        print('for loop start')
        for char in prefix:
            print(f'{node=}')
            node = node.get(char, None)
            if not node:
                print('False')
                return False
        print('for loop end')
        print(f'{node=}')
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
