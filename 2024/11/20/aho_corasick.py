from pprint import pprint, pformat
from collections import deque

bk = breakpoint

class TrieNode:
    def __init__(self, value=None, children=None, fail=None, output=None):
        self.value = value
        if not children:
            children = []
        self.children = children
        if not output:
            output = []
        self.output = output
        self.fail = fail

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curnode = self.root
        for char in word:
            for child in curnode.children:
                if child.value == char:
                    curnode = child
                    break
            else:
                new_node = TrieNode(char)
                curnode.children.append(new_node)
                curnode = new_node
        if curnode is not self.root:
            curnode.output.append(word)

def pre_process_trie(root):

    fail_node_mapping = {}
    # DECLARE free variable: root, fail_node_mapping
    def assign_failure_node(child, node):
        """assign fail node of child by revisiting parent's fail node
        until it ends up root
        """

        curnode = node
        value = child.value

        while curnode:
            # seek first on cache
            curnode = fail_node_mapping.get(curnode, root)

            for fail_node_candidate in curnode.children:
                if fail_node_candidate.value == value:
                    child.fail = fail_node_candidate
                    child.output.extend(fail_node_candidate.output)
                    fail_node_mapping[child] = fail_node_candidate
                    return fail_node_candidate

            if curnode is root:
                child.fail = root
                fail_node_mapping[child] = root
                return root

    queue = deque([])
    queue.extend(root.children)
    level = 0
    while queue:

        temp_storage = list(queue)
        queue.clear()

        if level == 0:
            for node in temp_storage:
                node.fail = root
                fail_node_mapping[node] = root
                for child in node.children:
                    assign_failure_node(child, node)
                queue.extend(node.children)
        else:
            for node in temp_storage:
                # process for intermediate node
                for child in node.children:
                    assign_failure_node(child, node)
                    pprint(fail_node_mapping)
                # process for the node itself (may be terminal node)

                queue.extend(node.children)
        level += 1


def word_list_to_trie(word_list):
    trie = Trie()
    for word in word_list:
        trie.insert(word)
    pre_process_trie(trie.root)
    return trie

def aho_corasick(sentence, word_list):
    trie = word_list_to_trie(word_list)
    root_node = trie.root
    curnode = trie.root
    result = set([])
    print_treenode(root_node)
    for idx, char in enumerate(sentence):
        for child in curnode.children:
            if child.value == char:
                curnode, result = update_curnode(child, result, idx)
                break
        else:
            # move along to fail chain
            # until reach root node
            found_along_fail_chain = False
            while not found_along_fail_chain and curnode is not root_node:
                curnode, result = update_curnode(curnode.fail, result, idx)
                for child in curnode.children:
                    if child.value == char:
                        curnode, result = update_curnode(child, result, idx)
                        found_along_fail_chain = True
                        break
    return result

def update_curnode(node, result, idx):
    if len(node.output):
        result |= set((idx, word) for word in node.output)
    return node, result

if __name__ == '__main__':
    # sentence = 'cdhisxy'
    # word_list = ['he', 'she', 'his', 'hers']
    sentence = 'dcabecab'
    word_list = ['ab', 'cabe', 'dcab']
    # word_list = ['ab']
    result = aho_corasick(sentence, word_list)
    print(result)
