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
  # print "# less", node_a, node_b
  # print_node(node_a)
  # print_node(node_b)
  if (freq[node_a] != freq[node_b]) {
    # print "# diff freq"
    # print freq[node_a] < freq[node_b]
    return freq[node_a] < freq[node_b]
  }
  # print "# leftmost"
  # print leftmost[node_a] < leftmost[node_b]
  return leftmost[node_a] < leftmost[node_b]
}

function parent(id) {
  # print "# parent", id
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
  # print "# find_swap_idx", id
  # print_node(id)
  if (!heap_left(id)) return ""
  # print "flag1"
  # print_node(heap_left(id))
  min_idx = heap_left(id)
  if (heap_right(id)) {
    # print "flag2"
    # print_node(heap_right(id))
    min_idx = less(heap[heap_left(id)], heap[heap_right(id)]) ? heap_left(id) : heap_right(id)
  }
  return less(heap[min_idx], heap[id]) ? min_idx : ""
}

function sift_down(id) {
  # print "# sift_down", id
  # print_node(id)
  if (find_swap_idx(id)) {
    # print "# flag", find_swap_idx(id)
    # print_node(find_swap_idx(id))
  }
  while ((swap_idx = find_swap_idx(id))) {
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
  # print "# before swap", 1, heap_n
  # print_node(heap[1])
  # print_node(heap[heap_n])
  heap_swap(1, heap_n)
  # print "# after swap", 1, heap_n
  # print_node(heap[1])
  # print_node(heap[heap_n])
  delete heap[heap_n]
  heap_n--
  # print "before sift_down"
  # print_heap()
  sift_down(1)
  # print "after sift_down"
  # print_heap()
  return node_id
}

function sift_up(id) {
  # print "# sift_up(" id ")"
  # if (!parent(id)) {
  #   print "no parent"
  #   return
  # }
  # print parent(id)
  while ((parent_idx = parent(id))) {
    # print parent_idx, parent(id)
    if (!less(heap[id], heap[parent_idx])) break
    heap_swap(id, parent_idx)
    id = parent_idx
  }
}

function heap_push(node_id) {
  # print "# heap_push(" node_id ")"
  heap[++heap_n] = node_id
  sift_up(heap_n)
}

function heappify() {
  for (i = int(heap_n / 2); i >= 1; i--) {
    sift_down(i)
  }
}

function print_heap() {
  for (i = 1; i <= heap_n; i++) {
    printf "%s: ", i
    print_node(heap[i])
  }
}

function new_node(ch, fq, le, ri, lm) {
  # print "# new_node"
  id++
  char[id] = ch
  freq[id] = fq
  left[id] = le ? le : 0
  right[id] = ri ? ri : 0
  leftmost[id] = lm ? lm : ch
  heap_push(id)
  return id
}

function print_node(id) {
  print id,char[id] ,freq[id] ,left[id] ,right[id] ,leftmost[id]
}

function swap(a, b,   t) { t = a; a = b; b = t }

function merge(node_a, node_b,   le, ri, lm) {
  ri = node_a; le = node_b
  if (less(node_a, node_b)) {
    le = node_a; ri = node_b
    lm = leftmost[node_a] < leftmost[node_b] ? leftmost[node_a] : leftmost[node_b]
  }
  return new_node("", freq[node_a] + freq[node_b], le, ri, lm)
}

function build_root(   root) {
  if (!heap_n) return ""
  if (heap_n == 1) return heap[1]
  while (heap_n > 1) {
    node_a = heap_pop()
    node_b = heap_pop()
    root = merge(node_a, node_b)
  }
  return root
}

function build_converter(node, prefix) {
  if (left[node] == 0 && right[node] == 0) converter[char[node]] = prefix
  if (left[node]) build_converter(left[node], prefix "0")
  if (right[node]) build_converter(right[node], prefix "1")
}

function encode(text,   n, ch, enc) {
  n = length(text)
  enc = ""
  for (i = 1; i <= n; i++) {
    ch = substr(text, i, 1)
    enc = enc converter[ch]
  }
  return enc
}

function decode(enc, root,   n, cur, code, text) {
  n = length(enc)
  cur = root
  text = ""
  for (i = 1; i <= n; i++) {
    code = substr(enc, i, 1)
    if (left[cur] == 0 && right[cur] == 0) {
      text = text char[cur]
      cur = root
      continue
    }
    cur = code == "0" ? left[cur] : right[cur]
  }
  return text
}

function print_converter() {
  for (ch in converter) {
    print ch, converter[ch]
  }
}

function print_root() {
}

NR == 1 {
  # print $0
  # print "flag0"
  n = length($0)
  # construct character counter
  for (i = 1; i <= n; i++) {
    ch = substr($0, i, 1)
    counter[ch] = counter[ch] ? counter[ch] + 1 : 1
  }
  # print "flag1"
  # init node
  for (ch in counter) {
    new_node(ch, counter[ch])
  }
  print_heap()
  while ((node_id = heap_pop())) {
    print_node(node_id)
  }
  # # print "flag2"
  # # build root
  # root = build_root()
  # print "flag3"
  # # build converter
  # build_converter(root, "")
  # print_converter()
  # print "flag4"
  # encode
  # enc = encode($0)
  # print enc
  # print "flag5"
  # # decode
  # text = decode(enc, root)
  # print text
}
