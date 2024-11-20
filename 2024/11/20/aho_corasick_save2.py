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

    def __repr__(self):
        return ''.join(self.gen_trie_repr())

    def gen_trie_repr(self):
        yield from '<trienode '
        # yield from f'{self.value}({id(self)})'
        yield from f'{self.value}'
        # yield '\n'
        if len(self.children):
            yield from ' children: ('
            yield from ','.join([child.value for child in self.children])
            yield ')'
            # yield '\n'
        if len(self.output):
            yield from ' output: ('
            yield from ','.join(self.output)
            yield ')'
            # yield '\n'
        if self.fail:
            yield from f' fail: ('
            # yield from f'{self.fail.value}({id(self.fail)})'
            yield from f'{self.fail.value if self.fail.value else "Root"}'
            yield ')'
        yield from ' >'

    def get_child_or_none(self):
        if len(self.children):
            return self.children[0]
        else:
            return None

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

def gen_order(tree_node):
    for child in tree_node.children:
        yield from gen_order(child)
    yield tree_node

def print_treenode(tree_node):
    for curnode in gen_order(tree_node):
        print(curnode)

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
        print(f'{queue=}')
        print(f'{level=}')

        temp_storage = list(queue)
        queue.clear()

        if level == 0:
            for node in temp_storage:
                node.fail = root
                fail_node_mapping[node] = root
                queue.extend(node.children)
        else:
            for node in temp_storage:
                for child in node.children:
                    assign_failure_node(child, node)
                queue.extend(node.children)
        level += 1

    print()
    pprint(fail_node_mapping)


if __name__ == '__main__':
    word_list = ['a', 'ab', 'ac', 'adab', 'adada']
    trie = Trie()
    for word in word_list:
        trie.insert(word)
    rootnode = trie.root
    # print_treenode(rootnode)
    pre_process_trie(rootnode)

    print_treenode(rootnode)
