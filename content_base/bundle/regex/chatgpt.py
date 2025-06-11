from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, EnumMeta, auto
from typing import List, Tuple, Optional

# ── 1. 상태 정의 ──────────────────────────────────────────────
class Special(Enum):
    SPLIT = auto()
    MATCH = auto()

@dataclass
class State:
    c: str | Special
    out: Optional["State"] = None
    out1: Optional["State"] = None

# ── 2.  “구멍 리스트” = (state, 필드이름) 튜플 목록 ─────────────
@dataclass
class Frag:
    start: State
    outs: List[Tuple[State, str]]          # ← 변경

def list1(pair: Tuple[State, str]) -> List[Tuple[State, str]]:
    return [pair]

def append(l1: List[Tuple[State, str]], l2: List[Tuple[State, str]]):
    return l1 + l2

def patch(outs: List[Tuple[State, str]], target: State):
    for st, attr in outs:
        setattr(st, attr, target)

# ── 3. 스택 조작 헬퍼 ─────────────────────────────────────────
def push(stack, frag): stack.append(frag)
def pop(stack):        return stack.pop()

# ── 4. 연산 구현 ──────────────────────────────────────────────
def character(stack, ch):
    s = State(ch)                           # out/out1 == None
    push(stack, Frag(s, list1((s, "out")))) # out 필드를 구멍으로 등록

def concat(stack):
    e2, e1 = pop(stack), pop(stack)
    patch(e1.outs, e2.start)
    push(stack, Frag(e1.start, e2.outs))

def alternate(stack):
    e2, e1 = pop(stack), pop(stack)
    s = State(Special.SPLIT, e1.start, e2.start)
    push(stack, Frag(s, append(e1.outs, e2.outs)))

def zero_or_one(stack):
    e = pop(stack)
    s = State(Special.SPLIT, e.start, None)
    push(stack, Frag(s, append(e.outs, list1((s, "out1")))))

def zero_or_more(stack):
    e = pop(stack)
    s = State(Special.SPLIT, e.start, None)
    patch(e.outs, s)
    push(stack, Frag(s, list1((s, "out1"))))

def one_or_more(stack):
    e = pop(stack)
    s = State(Special.SPLIT, e.start, None)
    patch(e.outs, s)
    push(stack, Frag(e.start, list1((s, "out1"))))

# ── 5. 후위표기 → NFA ────────────────────────────────────────
regex_map = {
    '.': concat,
    '|': alternate,
    '?': zero_or_one,
    '*': zero_or_more,
    '+': one_or_more,
}

def post2nfa(postfix: str) -> Optional[State]:
    stack: List[Frag] = []
    for tok in postfix:
        if tok in regex_map:
            regex_map[tok](stack)
        else:
            character(stack, tok)

    if len(stack) != 1:        # 잘못된 후위식 검증
        return None

    e = pop(stack)
    match = State(Special.MATCH)
    patch(e.outs, match)       # 남은 구멍을 전부 MATCH로
    return e.start

# ── 6. 빠른 확인 ─────────────────────────────────────────────
if __name__ == "__main__":
    import pprint
    nfa = post2nfa("abb.+.a.")   # (=  a (bb+). a .)
    pprint.pp(nfa)

