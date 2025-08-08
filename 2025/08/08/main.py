from fastapi import FastAPI
import uvicorn
import logging
from pydantic import BaseModel

logger = logging.getLogger()

class Req(BaseModel):
    arr: list

class LinkNode:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next_ = next_

    def __repr__(self):
        if self.next_:
            return f"{self.data} > {self.next_}"
        else:
            return f"{self.data}"

def arr2linkedlist(arr: list):
    n = len(arr)
    if len(arr) == 0:
        return LinkNode()

    head = curnode = LinkNode(arr[0])

    for idx in range(1, n):
        item = arr[idx]
        next_node = LinkNode(item)
        curnode.next_ = next_node
        curnode = next_node

    return head

def reverse(node: LinkNode):
    if node.next_ is None:
        return node
    head = cur = node
    nxt = node.next_
    while nxt.next_:
        prev, cur, nxt = cur, cur.next_, nxt.next_
        # logger.info(f"{prev.data=}, {cur.data=}, {nxt.data=}")
        # cur.next_ = prev
    head.next_ = None
    # nxt is the terminal node
    nxt.next_ = cur
    logger.info(f"{prev=}")
    logger.info(f"{cur=}")
    logger.info(f"{nxt=}")
    return nxt

def create_app():
    app_ = FastAPI()

    return app_

app = create_app()

@app.get("/")
def root():
    return {
        "message": "Hello World",
        "test": "here"
    }

@app.post("/reverse_linked_list")
def reverse_linked_list(req: Req):
    arr = req.arr
    ll = arr2linkedlist(arr)
    logger.info(ll)
    rev = reverse(ll)
    logger.info(rev)
    return rev

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_config="log_config.yml")
