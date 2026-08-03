# heap.awk
# struct {
#   left: node,
#   right: node,
#   char: str,
#   freq: int,
#   leftmost: char
# } node
# each node has node_id
#
# heap_n: length(heap)
# heap: consists of node_id
function less(node_a, node_b) {
  if (freq[node_a] != freq[node_b]) {
    return freq[node_a] < freq[node_b]
  }
  return char[node_a] < char[node_b]
}

function parent(id) {
  return id == 1 ? "" : int(id / 2)
}

function heap_left(id) {
  return id * 2 > heap_n ? "" : id * 2
}

function heap_right(id) {
  return (id * 2 + 1) > heap_n ? "" : id * 2 + 1
}

function heap_swap(a, b,   t) {
  t = heap[a]
  heap[a] = heap[b]
  heap[b] = t
}

function find_swap_idx(id,   min_idx) {
  if (!heap_left(id)) return ""
  min_idx = heap_left(id)
  if (heap_right(id) && less(min_idx, heap_right(id))) {
    min_idx = heap_right(id)
  }
  return less(min_idx, id) ? min_idx : ""
}

function sift_down(id) {
  while((swap_idx = find_swap_idx(id))) {
    heap_swap(id, swap_idx)
    id = swap_idx
  }
}

function heap_pop(   node_id) {
  if (heap_n == 0) return ""
  node_id = heap[1]
  if (heap_n == 1) {
    delete heap[1]
    heap_n--
    return node_id
  }
  heap_swap(1, heap_n)
  delete heap[heap_n]
  heap_n--
  sift_down(1)
  return node_id
}

function sift_up(id) {
  while ((parent_idx = parent(id))) {
    if (!less(id, parent_idx)) break
    heap_swap(id, parent_idx)
  }
}

function heap_push(node_id) {
  heap[++heap_n] = node_id
  sift_up(heap_n)
}

function heappify() {
  for (i = int(heap_n / 2); i >= 1; i--) {
    sift_down(i)
  }
}

function new_node(ch, fq, le, ri, lm) {
  id++
  char[id] = ch
  freq[id] = fq
  left[id] = le ? le : 0
  right[id] = ri ? ri : 0
  leftmost[id] = lm ? lm : ch
  heap_push(id)
}

function swap(a, b,   t) { t = a; a = b; b = t }

function merge(node_a, node_b,   le, ri, lm) {
  ri = node_a; le = node_b
  if (less(node_a, node_b)) {
    le = node_a; ri = node_b
    lm = leftmost[node_a] < leftmost[node_b] ? leftmost[node_a] : leftmost[node_b]
  }
  new_node("", freq[node_a] + freq[node_b], le, ri, lm)
}


