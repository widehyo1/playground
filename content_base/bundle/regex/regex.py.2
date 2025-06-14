from pprint import pprint, pformat
from collections.abc import Sequence
from typing import Optional
from dataclasses import dataclass
from enum import Enum, EnumMeta


class SpecialState(Enum):
    SPLIT = 256
    MATCH = 257
    EMPTY = 258


class _RegexOpMeta(EnumMeta):
    def __contains__(self, item):
        if isinstance(item, self):
            return True
        return item in (
            member.value for member in self
        )  # short circuit: O(k), k <= n, memory O(1)
        # return item in {member.value for member in self} # constructing set: O(n), and lookup O(1) for time, memory O(n)


class RegexOp(Enum, metaclass=_RegexOpMeta):
    CONCAT = "."
    ALTERNATIVE = "|"
    ZERO_OR_MORE = "*"
    ONE_OR_MORE = "+"
    ZERO_OR_ONE = "?"

    # @classmethod
    # def to_set(cls):
    #     return {member.value for member in cls}


@dataclass
class State:
    c: str | SpecialState
    out: Optional["State"] = None
    out1: Optional["State"] = None

    @classmethod
    def empty(cls):
        return State(SpecialState.EMPTY, None, None)

    def to_list(self):
        return [self]


@dataclass
class Frag:
    start: State
    out: Sequence[State]

    def patch(self, s: State):
        for state in self.out:
            state.out = s


def _chain(l1: Sequence[State], l2: Sequence[State]):
    yield from l1
    yield from l2


def chain(l1: Sequence[State], l2: Sequence[State]):
    return [item for item in _chain(l1, l2)]


def one_or_more(stack):
    e = stack.pop()
    s = State(SpecialState.SPLIT, e.start, State.empty())
    e.out = s.to_list()
    stack.append(Frag(e.start, s.out1.to_list()))


def zero_or_one(stack):
    e = stack.pop()
    s = State(SpecialState.SPLIT, e.start, State.empty())
    stack.append(Frag(s, chain(e.out, s.out1.to_list())))


def zero_or_more(stack):
    e = stack.pop()
    s = State(SpecialState.SPLIT, e.start, State.empty())
    e.out = s.to_list()
    stack.append(Frag(s, s.out1.to_list()))


def alternative(stack):
    e1 = stack.pop()
    e2 = stack.pop()
    s = State(SpecialState.SPLIT, e1.start, e2.start)
    stack.append(Frag(s, chain(e1.out, e2.out)))


def concat(stack):
    e1 = stack.pop()
    e2 = stack.pop()
    e1.patch(e2.start)
    stack.append(Frag(e1.start, e2.out))


def character(stack, char):
    s = State(char, State.empty(), State.empty())
    stack.append(Frag(s, s.out.to_list()))


def post2nfa(postfix: str) -> State | None:

    stack = []

    regex_mapping = {
        "+": one_or_more,
        "*": zero_or_more,
        "?": zero_or_one,
        "|": alternative,
        ".": concat,
    }

    for p in postfix:
        if p in RegexOp:
            regex_mapping[p](stack)
        else:
            character(stack, p)

    e = stack.pop()
    if len(stack) != 0:
        pprint(stack)
        print("invaild postfix")
        return None
    e.patch(State(SpecialState.MATCH, State.empty(), State.empty()))

    return e.start


if __name__ == "__main__":
    postfix = "abb.+.a."
    nfa = post2nfa(postfix)
    pprint(nfa)
