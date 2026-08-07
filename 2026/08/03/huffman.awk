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
function less(na, nb) {
  if (freq[na] != freq[nb]) {
    return freq[na] < freq[nb]
  }
  return leftmost[na] < leftmost[nb]
}

function heap_less(ha, hb) {
  return less(heap[ha], heap[hb])
}

function parent(idx) {
  return idx == 1 ? "" : int(idx / 2)
}

function heap_left(idx) {
  return idx * 2 > heap_n ? "" : idx * 2
}

function heap_right(idx) {
  return (idx * 2 + 1) > heap_n ? "" : idx * 2 + 1
}

function heap_swap(a, b,   t) {
  t = heap[a]
  heap[a] = heap[b]
  heap[b] = t
}

function find_swap_idx(idx,   min_idx) {
  if (!heap_left(idx)) return ""
  min_idx = heap_left(idx)
  if (heap_right(idx) && heap_less(heap_right(idx), min_idx)) {
    min_idx = heap_right(idx)
  }
  return heap_less(min_idx, idx) ? min_idx : ""
}

function sift_down(idx) {
  while ((swap_idx = find_swap_idx(idx))) {
    heap_swap(idx, swap_idx)
    idx = swap_idx
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

function sift_up(idx) {
  while ((parent_idx = parent(idx))) {
    if (!heap_less(idx, parent_idx)) break
    heap_swap(idx, parent_idx)
    idx = parent_idx
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

function print_heap() {
  for (i = 1; i <= heap_n; i++) {
    printf "%s: ", i
    print_node(heap[i])
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
  return id
}

function print_node(id) {
  print id, char[id], freq[id], left[id], right[id], leftmost[id]
}

function swap(a, b,   t) { t = a; a = b; b = t }

function merge(na, nb,   le, ri, lm) {
  ri = na; le = nb
  if (less(na, nb)) {
    le = na; ri = nb
    lm = leftmost[na] < leftmost[nb] ? leftmost[na] : leftmost[nb]
  }
  return new_node("", freq[na] + freq[nb], le, ri, lm)
}

function build_root(   root) {
  if (!heap_n) return ""
  if (heap_n == 1) return heap[1]
  while (heap_n > 1) {
    na = heap_pop()
    nb = heap_pop()
    root = merge(na, nb)
  }
  return root
}

function build_converter(node, prefix) {
  if (left[node] == 0 && right[node] == 0) {
    encoder[char[node]] = prefix
    decoder[prefix] = char[node]
  }
  if (left[node]) build_converter(left[node], prefix "0")
  if (right[node]) build_converter(right[node], prefix "1")
}

function encode(text,   n, ch, enc) {
  n = length(text)
  enc = ""
  for (i = 1; i <= n; i++) {
    ch = substr(text, i, 1)
    enc = enc encoder[ch]
  }
  return enc
}

function decode(enc, root,   n, code, text) {
  n = length(enc)
  text = ""
  code = ""
  for (i = 1; i <= n; i++) {
    code = code substr(enc, i, 1)
    if (code in decoder) {
      text = text decoder[code]
      code = ""
      continue
    }
  }
  return text
}

function print_encoder() {
  for (ch in encoder) {
    print ch, encoder[ch]
  }
}

function print_decoder() {
  for (code in decoder) {
    print code, decoder[code]
  }
}

NR == 1 {
  n = length($0)
  # construct character counter
  for (i = 1; i <= n; i++) {
    ch = substr($0, i, 1)
    counter[ch] = counter[ch] ? counter[ch] + 1 : 1
  }
  # init node
  for (ch in counter) {
    new_node(ch, counter[ch])
  }
  print_heap()
  # while ((node_id = heap_pop())) {
  #   print_node(node_id)
  # }
  # build root
  root = build_root()
  # build encoder
  build_converter(root, "")
  print_encoder()
  print_decoder()
  enc = encode($0)
  print enc
  # decode
  text = decode(enc, root)
  print text
}
