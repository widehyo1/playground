"""
a python version code for d3-hierachy code
"""
from dataclassed import dataclass
from typing import Optional, List
from collections.abc import Callable
from itertools import deque


@dataclass
class Node:
    data: dict,
    depth: Optional[int] = 0
    height: Optional[int] = 0
    parent: Optional["Node"] = None
    children: Optional[List["Node"]] = None

    def __post_init__(self):
        self.children = self.children or []

    def __iter__(self):
        return self

    def __next__(self):
        """
        iterates node by BFS
        ```js
        export default function*() {
          var node = this, current, next = [node], children, i, n;
          do {
            current = next.reverse(), next = [];
            while (node = current.pop()) {
              yield node;
              if (children = node.children) {
                for (i = 0, n = children.length; i < n; ++i) {
                  next.push(children[i]);
                }
              }
            }
          } while (next.length);
        }
        ```
        """
        stock = [self]
        while stock:
            queue = stock[::-1] # not using queue version
            # queue = deque(stock[::]) # using queue version
            stock = []
            while queue:
                cur_node = queue.pop() # not using queue version
                # cur_node = queue.popleft() # using queue version
                yield cur_node
                stock.extend(cur_node.children)

    @classmethod
    def from_data(cls, data: dict):
        """

```js
export default function hierarchy(data, children) {
    if (data instanceof Map) {
        data = [undefined, data];
        if (children === undefined) children = mapChildren;
    } else if (children === undefined) {
        children = objectChildren;
    }

    var root = new Node(data),
        node,
        nodes = [root],
        child,
        childs,
        i,
        n;

        while (node = nodes.pop()) {
            if ((childs = children(node.data)) && (n = (childs = Array.from(childs)).length)) {
                node.children = childs;
                for (i = n - 1; i >= 0; --i) {
                    nodes.push(child = childs[i] = new Node(childs[i]));
                    child.parent = node;
                    child.depth = node.depth + 1;
                }
            }
        }

        return root.eachBefore(computeHeight);
}
```
        """
        root = Node(data)
        queue = [root]
        while queue:
            cur_node = queue.pop()
            children = cur_node.data.get("children", [])
            for child in children[::-1]:
                child_node = Node(child)
                child_node.parent = cur_node
                child_node.depth = cur_node.depth + 1
                cur_node.children.append(child_node)
                queue.append(child_node)

        # return root.eachBefore(computeHeight);

        # export function computeHeight(node) {
        #   var height = 0;
        #   do node.height = height;
        #   while ((node = node.parent) && (node.height < ++height));
        # }

        for it_node in root:
            # BFS 방식으로 순회하되
            height = 0
            it_node.height = height
            while it_node.parent:
                # 상위 노드가 존재할 때
                it_node = it_node.parent
                height += 1
                # 상위 노드의 height는 여러 children 중
                if it_node.height < height:
                    # 자신을 처음으로 방문한 경우에만 증가한다.
                    # len(node.children) = 3인 node의 경우
                    # 3개의 child 중 BFS 방식으로 가장 먼저 방문한 child에 의해서만
                    # height가 증가하고
                    it_node.height = height
                else:
                    # 나머지 child에 대해서는 height가 변하지 않는다.
                    # 이 경우 BFS의 다음 노드를 대상으로 순회한다.
                    break

        return root


    def count(self):
        ...

    def each(self):
        ...

    def eachAfter(self, func: Callable):
"""
마지막 원소 우선 DFS 방식으로 순회한다.
함수의 적용은 각 순회 이후에 한다.
```js
export default function(callback, that) {
  var node = this, nodes = [node], next = [], children, i, n, index = -1;
  while (node = nodes.pop()) {
    next.push(node);
    if (children = node.children) {
      for (i = 0, n = children.length; i < n; ++i) {
        nodes.push(children[i]);
      }
    }
  }
  while (node = next.pop()) {
    callback.call(that, node, ++index, this);
  }
  return this;
}
```

이 부분 stack이다.
  while (node = nodes.pop()) {
    next.push(node);
    if (children = node.children) {
      for (i = 0, n = children.length; i < n; ++i) {
        nodes.push(children[i]);
      }
    }
  }
"""
        stack = [self]
        store = []
        while stack:
            cur_node = stack.pop()
            store.append(cur_node)
            for child in cur_node.children:
                stack.append(child)

        for it_node in store:
            func(cur_node)

    def eachBefore(self, func: Callable):
"""
첫 번째 원소 우선 DFS 방식으로 순회한다.
함수의 적용은 각 순회 전에 한다.
```js
export default function(callback, that) {
  var node = this, nodes = [node], children, i, index = -1;
  while (node = nodes.pop()) {
    callback.call(that, node, ++index, this);
    if (children = node.children) {
      for (i = children.length - 1; i >= 0; --i) {
        nodes.push(children[i]);
      }
    }
  }
  return this;
}
```
"""
        stack = [self]
        while stack:
            cur_node = stack.pop()
            func(cur_node)
            stack.extend(cur_node.children[::-1])

    def find(self, predicate: Callable):
"""
자신 및 하위 노드를 BFS 방식으로 순회하되,
predicate인 function을 인수로 받아 true인 첫 node를 반환한다.
```js
export default function(callback, that) {
  let index = -1;
  for (const node of this) {
    if (callback.call(that, node, ++index, this)) {
      return node;
    }
  }
}
```
"""
    for it_node in root:
        if predicate(it_node):
            return it_node

    def sum(self, get_value: Callable):
"""
이게 맞나?
value는 node.data에서 어떠한 값을 추출하는 함수인 것 같다.
```js
export default function(value) {
  return this.eachAfter(function(node) {
    var sum = +value(node.data) || 0,
        children = node.children,
        i = children && children.length;
    while (--i >= 0) sum += children[i].value;
    node.value = sum;
  });
}
```
"""
        stack = [self]
        dfs_visit_order = []
        while stack:
            cur_node = stack.pop()
            for child in cur_node.children:
                dfs_visit_order.append(child)

        for it_node in dfs_visit_order:
            it_node.value = value(it_node.data)
            for it_child in it_node.children:
                it_node.value += value(it_child.data)

    def sum2(self, get_value: Callable):
"""
이게 맞나?
value는 node.data에서 어떠한 값을 추출하는 함수인 것 같다.
```js
export default function(value) {
  return this.eachAfter(function(node) {
    var sum = +value(node.data) || 0,
        children = node.children,
        i = children && children.length;
    while (--i >= 0) sum += children[i].value;
    node.value = sum;
  });
}
```
"""
        stack = [self]
        dfs_visit_order = []
        acc = 0
        while stack:
            cur_node = stack.pop()
            acc += value(cur_node.data)
            for child in cur_node.children:
                dfs_visit_order.append(child)

        self.value = acc

    def sort(self, comparator: Callable):
"""
```js
export default function(compare) {
  return this.eachBefore(function(node) {
    if (node.children) {
      node.children.sort(compare);
    }
  });
}
```
"""
        stack = [self]
        while stack:
            cur_node = stack.pop()
            cur_node.children.sort(key=comparator)
            for child in cur_node.children[::-1]:
                stack.append(child)

    def path(self):
        ...

    def ancestors(self):
        ...

    def descendants(self):
        ...

    def leaves(self):
        ...

    def links(self):
        ...

    def copy(self):
        ...
