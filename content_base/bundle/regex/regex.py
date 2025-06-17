from dataclasses import dataclass
from collections import deque
from typing import Sequence, Tuple, Optional
from enum import Enum, auto
from pprint import pp
import sys


class Special(Enum):
    SPLIT = auto()
    MATCH = auto()


@dataclass
class State:
    c: str | Special
    out: Optional["State"] | None = None
    out1: Optional["State"] | None = None

    def to_tuple(self, attrname) -> Sequence[Tuple["State", str]]:
        return [(self, attrname)]

    def __hash__(self):
        return id(self)

    def ismatch(self):
        visited = set()
        stack = [self]

        while stack:
            state = stack.pop()
            if state in visited:
                continue
            visited.add(state)
            if state.c == Special.MATCH:
                return True
            elif state.c == Special.SPLIT:
                stack.append(state.out)
                stack.append(state.out1)
            elif state.out:
                stack.append(state.out)

        return False
    
    def extract_graph(self) -> dict:
        visited = set()
        node_inventory = {}
        stack = [(self, None, None)]
        nodes = []
        edges = []
        split_nodes = []
        match_nodes = []
        nodeid = 0
        while stack:
            state, parent, parentid = stack.pop()
            if state in visited:
                edges.append((parentid, node_inventory[state]))
                continue
            nodeid += 1
            visited.add(state)
            node_inventory[state] = nodeid
            edges.append((parentid, nodeid))

            if state.out:
                stack.append((state.out, state, nodeid))
            if state.out1:
                stack.append((state.out1, state, nodeid))

            if state.c == Special.MATCH:
                nodes.append((nodeid, ""))
                match_nodes.append(nodeid)
            elif state.c == Special.SPLIT:
                nodes.append((nodeid, ""))
                split_nodes.append(nodeid)
            else:
                nodes.append((nodeid, state.c))

        return {
            "nodes": nodes,
            "match_nodes": match_nodes,
            "split_nodes": split_nodes,
            "edges": edges,
        }

    def to_dot(self):
        graph_info = self.extract_graph()
        print("\n".join(generate_dotfile(graph_info)))

def generate_dotfile(graph_info: dict):
    nodes = graph_info["nodes"]
    matches = graph_info["match_nodes"]
    splits = graph_info["split_nodes"]
    edges = graph_info["edges"]
    yield 'digraph {'
    yield '  fontname="Helvetica,Arial,snas-serif"'
    yield '  node [fontname="Helvetica,Arial,snas-serif"]'
    yield '  edge [fontname="Helvetica,Arial,snas-serif"]'
    yield ''
    yield '  graph [center=1 rankdir=LR]'
    yield ''
    yield '  node [height=0.25 width=0.25 shape="circle" label=""]'
    yield '  node [shape="doublecircle"] ' + " ".join([f"n{id_:03}" for id_ in matches])
    yield '  node [shape="point"] ' + " ".join([f"n{id_:03}" for id_ in splits])
    yield '  node [shape="circle"]'
    yield ''
    yield from [f'  n{id_:03} [label="{c}"]' for id_, c in nodes]
    yield ''
    yield from [f'  n{from_:03} -> n{to:03}' for from_, to in edges if from_ is not None]
    yield '}'

@dataclass
class Frag:
    start: State
    outs: Sequence[Tuple[State, str]]


@dataclass
class Scope:
    atom_cnt: int = 0
    alt_cnt: int = 0


@dataclass
class StateWalker:
    state: State

    @classmethod
    def from_state(cls, state: State) -> "StateWalker":
        return StateWalker(state)

    def state_generator(self, maxlevel: int | None = None):
        queue = deque([(self.state, 0)])
        while queue:
            st, step_level = queue.popleft()

            if maxlevel is not None and step_level > maxlevel:
                continue

            yield st, step_level
            if st.c == Special.SPLIT:
                queue.append((st.out, step_level))
                queue.append((st.out1, step_level))
            elif st.out:
                queue.append((st.out, step_level + 1))

    def gen_filter(self, string: str):
        for idx, char in enumerate(string):
            for st, step_level in self.state_generator(idx):
                if idx == step_level and st.c == char:
                    yield (st, step_level)

    def ismatch(self, string) -> bool:
        target = len(string) - 1

        return any(
            st.ismatch()
            for st, step_level in self.gen_filter(string)
            if step_level == target
        )


def patch(outs: Sequence[Tuple[State, str]], target: State):
    for state, attr in outs:
        setattr(state, attr, target)


def append(
    s1: Sequence[Tuple[State, str]], s2: Sequence[Tuple[State, str]]
) -> Sequence[Tuple[State, str]]:
    return s1 + s2


def zero_or_more(stack):
    e = stack.pop()
    s = State(Special.SPLIT, e.start, None)
    patch(e.outs, s)
    stack.append(Frag(s, s.to_tuple("out1")))


def one_or_more(stack):
    e = stack.pop()
    s = State(Special.SPLIT, e.start, None)
    patch(e.outs, s)
    stack.append(Frag(e.start, s.to_tuple("out1")))


def zero_or_one(stack):
    e = stack.pop()
    s = State(Special.SPLIT, e.start, None)
    stack.append(Frag(s, append(e.outs, s.to_tuple("out1"))))


def concat(stack):
    e1 = stack.pop()
    e2 = stack.pop()
    patch(e2.outs, e1.start)
    stack.append(Frag(e2.start, e1.outs))


def alternate(stack):
    e1 = stack.pop()
    e2 = stack.pop()
    s = State(Special.SPLIT, e1.start, e2.start)
    stack.append(Frag(s, append(e1.outs, e2.outs)))


def character(stack, tok: str):
    s = State(tok)
    stack.append(Frag(s, s.to_tuple("out")))


def post2nfa(postfix) -> State | None:

    stack: Sequence[Frag] = []

    for tok in postfix:
        match tok:
            case "*": zero_or_more(stack)
            case "+": one_or_more(stack)
            case "?": zero_or_one(stack)
            case ".": concat(stack)
            case "|": alternate(stack)
            case _: character(stack, tok)

    assert len(stack) == 1, "invalid postfix"
    e = stack.pop()
    matchstate = State(Special.MATCH)
    patch(e.outs, matchstate)
    return e.start


def flush_atom(scope, postfix_buffer):
    if scope.atom_cnt > 0:
        postfix_buffer += ["."] * (scope.atom_cnt - 1)
    scope.atom_cnt = 0
    return postfix_buffer


def flush_scope(scope, postfix_buffer):
    postfix_buffer = flush_atom(scope, postfix_buffer)
    postfix_buffer += ["|"] * scope.alt_cnt
    scope.alt_cnt = 0
    return postfix_buffer


def re2post(regex: str) -> str:
    """
    a(bb)+a -> abb.+.a.
    """

    postfix_buffer = []
    stack = [Scope()]
    scope_level = 0
    scope = stack[scope_level]
    for re in regex:
        match re:
            case "*" | "+" | "?":
                postfix_buffer.append(re)
            case "(":
                if scope.atom_cnt > 1:
                    scope.atom_cnt -= 1
                    postfix_buffer.append(".")
                scope_level += 1
                stack.append(Scope())
                scope = stack[scope_level]
            case ")":
                assert scope_level != 0, "closing paren - can not close unopened paren"
                assert scope.atom_cnt != 0, "closing paren - atom is empty"
                postfix_buffer = flush_scope(scope, postfix_buffer)
                scope_level -= 1
                scope = stack[scope_level]
                scope.atom_cnt += 1
            case "|":
                assert scope.atom_cnt != 0, "alternate - atom is empty"
                postfix_buffer = flush_atom(scope, postfix_buffer)
                scope.alt_cnt += 1
            case _:
                if scope.atom_cnt > 1:
                    scope.atom_cnt -= 1
                    postfix_buffer.append(".")
                postfix_buffer.append(re)
                scope.atom_cnt += 1
    assert scope_level == 0, "invalid paren - unclosed paren"
    postfix_buffer = flush_scope(scope, postfix_buffer)

    return "".join(postfix_buffer)


def regex_by_nfa(regex, string):
    postfix = re2post(regex)
    nfa = post2nfa(postfix)
    sw = StateWalker.from_state(nfa)
    return sw.ismatch(string)

def print_dot(regex):
    postfix = re2post(regex)
    nfa = post2nfa(postfix)
    nfa.to_dot()


# main
if __name__ == "__main__":
    # regex = "a+"
    # for string in ["", "a", "aa", "aaa", "asve"]:
    #     print(regex_by_nfa(regex, string))
    # regex = "a(bb)+a|ab*ab"
    regexes = ["a+", "a?b+c*", "ab|cd", "((a|b)c)*", "a(b|c)*d", "a(b(cd)?)+", "a(bb)+a|ab*ab"]
    target = int(sys.argv[1])
    print_dot(regexes[target])
