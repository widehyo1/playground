from pprint import pprint, pformat

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
        yield from f'{self.value}({id(self)})'
        yield '\n'
        yield from 'children: ('
        if len(self.children):
            yield from ','.join([child.value for child in self.children])
        else:
            yield '-'
        yield ')'
        yield '\n'
        yield from 'output: ('
        if len(self.output):
            yield from ','.join(self.output)
        else:
            yield '-'
        yield ')'
        yield '\n'
        yield from f'fail: ('
        if self.fail:
            yield from '{self.fail.value}({id(self.fail)})'
        else:
            yield '-'
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

def gen_order(tree_node):
    for child in tree_node.children:
        yield from gen_order(child)
    yield tree_node

def print_treenode(tree_node):
    for curnode in gen_order(tree_node):
        print(curnode)

if __name__ == '__main__':
    word_list = ['a', 'ab', 'ac', 'adab', 'adada']
    trie = Trie()
    print(trie.root)
    for word in word_list:
        trie.insert(word)
    print(trie.root)
    print_treenode(trie.root)
    rootnode = trie.root
    a = rootnode.children[0]
    ab = a.children[0]
    ac = a.children[1]
    ad = a.children[2]
    ada = ad.children[0]
    adab = ada.children[0]
    adad = ada.children[1]
    adada = adad.children[0]
    bk()
