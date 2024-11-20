from collections import deque

class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = {}  # Use a dictionary for O(1) access
        self.fail = None
        self.output = []

    def __repr__(self):
        return f'<TrieNode({self.value}) children={list(self.children.keys())} fail={self.fail.value if self.fail else "Root"} output={self.output}>'

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curnode = self.root
        for char in word:
            if char not in curnode.children:
                curnode.children[char] = TrieNode(char)
            curnode = curnode.children[char]
        curnode.output.append(word)

def build_failure_links(root):
    queue = deque()
    for child in root.children.values():
        child.fail = root
        queue.append(child)

    while queue:
        current_node = queue.popleft()
        for char, child in current_node.children.items():
            # Set failure link
            fail_node = current_node.fail
            while fail_node and char not in fail_node.children:
                fail_node = fail_node.fail
            child.fail = fail_node.children[char] if fail_node else root
            child.output.extend(child.fail.output)
            queue.append(child)

def aho_corasick(sentence, word_list):
    # Build Trie and preprocess failure links
    trie = Trie()
    for word in word_list:
        trie.insert(word)
    build_failure_links(trie.root)

    # Search in the sentence
    curnode = trie.root
    results = []

    for idx, char in enumerate(sentence):
        # Follow fail links for mismatches
        while curnode is not trie.root and char not in curnode.children:
            curnode = curnode.fail
        
        # Move to the next state
        curnode = curnode.children.get(char, trie.root)

        # Collect matches
        if curnode.output:
            return True
            # for pattern in curnode.output:
            #     start_idx = idx - len(pattern) + 1
            #     results.append((start_idx, pattern))

    # return results
    return False

n = 3
# word_list = [input() for _ in range(n)]
word_list = [ "www", "woo", "jun" ]
# m = int(input())
m = 3
# sentences = [input() for _ in range(m)]
sentences = [ "myungwoo", "hongjun", "dooho" ]

for sentence in sentences:
    print("YES" if aho_corasick(sentence, word_list) else "NO")

# if __name__ == '__main__':
#     sentence = 'dcabecab'
#     word_list = ['ab', 'cabe', 'dcab']
#     result = aho_corasick(sentence, word_list)
#     print(result)
