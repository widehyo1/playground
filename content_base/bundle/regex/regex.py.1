from collections.abc import Sequence
from typing import Optional
from enum import Enum, auto
from dataclasses import dataclass


class ReprMixin:
    hide_fields = set()

    def _get_debug_fields(self):
        return {k: v for k, v in self.__dict__.items() if k not in hide_fields}

    def __repr__(self):
        from pprint import pformat

        fields = self._get_debug_fields()
        formatted = ", ".join(f"{k}={pformat(v)}" for k, v in fields.items())
        return f"<{self.__class__.__name__} {formatted}>"


class Node(Enum):
    Split = 256
    Match = 257


StateType = Optional["State"]
PtrType = Optional["Ptrlist"]
FragType = Optional["Frag"]

nstate = 0


@dataclass
class State(ReprMixin):
    """
    Represents an NFA state plus zero or one or two arrows exiting.
    if c == Match, no arrows out; matching state.
    If c == Split, unlabeled arrows to out and out1 (if != NULL).
    If c < 256, labeled arrow with character c to out.
    """

    c: int
    out: StateType = None
    out1: StateType = None
    lastlist: int = 0

    def __post_init__(self):
        global nstate
        nstate += 1
        print(f"current nstate: {nstate}")


print("init match_state")
match_state = State(Node.Match.value)
nstate -= 1
print(f"done with nstate: {nstate}")


@dataclass
class Frag(ReprMixin):
    """
    A partially built NFA without the matching state filled in.
    Frag.start points at the start state.
    Frag.out is a list of places that need to be set to the
    next state for this fragment.
    """

    start: StateType = None
    out: PtrType = None


@dataclass
class Ptrlist(ReprMixin):
    """
    Since the out pointers in the list are always
    uninitialized, we use the pointers themselves
    as storage for the Ptrlists.
    """

    nxt: PtrType = None
    s: StateType = None

    @classmethod
    def from_states(cls, outp: Optional[Sequence["State"]]) -> PtrType:
        if outp:
            return Ptrlist(None, outp)
        return None


def patch(l: PtrType, s: StateType) -> None:
    while l:
        next_l = l.nxt
        l.s = s
        l = next_l


def append(l1: PtrType, l2: PtrType) -> PtrType:
    head = l1
    while l1.nxt:
        l1 = l1.nxt
    l1.nxt = l2
    return head


def post2nfa(postfix: str) -> StateType:

    if len(postfix) == 0:
        return None

    list1 = Ptrlist.from_states
    stack = []

    # closures for free variable stack:
    # concat, alternate, zero_or_one,
    # zero_or_more, one_or_more, character
    # get_processor
    def concat(char=None):
        e2 = stack.pop()
        e1 = stack.pop()
        print(f"e2: {e2}, e1: {e1}")
        patch(e1.out, e2.start)
        stack.append(Frag(e1.start, e2.out))

    def alternate(char=None):
        e2 = stack.pop()
        e1 = stack.pop()
        s = State(Node.Split.value, e1.start, e2.start)
        stack.append(Frag(s, append(e1.out, e2.out)))

    def zero_or_one(char=None):
        e = stack.pop()
        s = State(Node.Split.value, e.start, None)
        stack.append(Frag(s, append(e.out, list1(s.out1))))

    def zero_or_more(char=None):
        e = stack.pop()
        s = State(Node.Split.value, e.start, None)
        patch(e.out, s)
        stack.append(Frag(s, list1(s.out1)))

    def one_or_more(char=None):
        e = stack.pop()
        s = State(Node.Split.value, e.start, None)
        patch(e.out, s)
        stack.append(Frag(e.start, list1(s.out1)))

    def character(char):
        s = State(ord(char), None, None)
        stack.append(Frag(s, list1(s.out)))

    special_chars = {".", "|", "?", "*", "+"}
    processor_inventory = {
        ".": concat,
        "|": alternate,
        "?": zero_or_one,
        "*": zero_or_more,
        "+": one_or_more,
    }

    def get_processor(char):
        if char not in special_chars:
            return character
        return processor_inventory[char]

    for p in postfix:
        print("postfix loop")
        print(p, stack)
        processor = get_processor(p)
        processor(p)

    e = stack.pop()
    if len(stack):
        return None

    global match_state

    patch(e.out, match_state)
    return e.start


if __name__ == "__main__":
    postfix = "abb.+.a."
    res = post2nfa(postfix)
    print("main result:")
    print(res)
