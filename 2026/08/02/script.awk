# huffman.awk
# input: one-liner string
# struct {
#   left,
#   right,
#   char,
#   freq,
#   leftmost
# } node
# leftmost for tie-break

function less(node_a, node_b) {
  if (freq[node_a] != freq[node_b]) {
    return freq[node_a] < freq[node_b]
  }
  return leftmost[node_a] < leftmost[node_b]
}

function out_less(node_a, node_b) {
  if (out_freq[node_a] != out_freq[node_b]) {
    return out_freq[node_a] < out_freq[node_b]
  }
  return out_leftmost[node_a] < out_leftmost[node_b]
}

function swap_left(a, b,   t) { t = left[a]; left[a] = left[b]; left[b] = t }
function swap_right(a, b,   t) { t = right[a]; right[a] = right[b]; right[b] = t }
function swap_char(a, b,   t) { t = char[a]; char[a] = char[b]; char[b] = t }
function swap_freq(a, b,   t) { t = freq[a]; freq[a] = freq[b]; freq[b] = t }
function swap_leftmost(a, b,   t) { t = leftmost[a]; leftmost[a] = leftmost[b]; leftmost[b] = t }

function heap_swap(node_a, node_b) {
  swap_left(node_a, node_b)
  swap_right(node_a, node_b)
  swap_char(node_a, node_b)
  swap_freq(node_a, node_b)
  swap_leftmost(node_a, node_b)
}

function heap_out(node) {
  heap_out_n++
  out_left[heap_out_n] = left[node]
  out_right[heap_out_n] = right[node]
  out_char[heap_out_n] = char[node]
  out_freq[heap_out_n] = freq[node]
  out_leftmost[heap_out_n] = leftmost[node]
}

function heap_left(node) {
  return node * 2 > heap_n ? "" : node * 2
}

function heap_right(node) {
  return node * 2 + 1 > heap_n ? "" : node * 2 + 1
}

function heap_parent(node) {
  return node == 1 ? "" : int(node / 2)
}

function find_swap_idx(node,   min_idx) {
  if (!heap_left(node)) return
  if (heap_left(node)) {
    if (heap_right(node)) {
      min_idx = less(heap_left(node), heap_right(node)) ? heap_left(node) : heap_right(node)
      if (less(min_idx, node)) return min_idx
    } else {
      if (less(heap_left(node), node)) return heap_left(node)
    }
  }
}

function sift_down(node,   swap_idx) {
  while ((swap_idx = find_swap_idx(node))) {
    heap_swap(swap_idx, node)
    node = swap_idx
  }
}

function sift_up(node) {
  while (less(node, heap_parent(node))) {
    heap_swap(node, heap_parent(node))
    node = heap_parent(node)
  }
}

function heap_push(c, count, left_node, right_node, lm) {
  heap_n++
  char[heap_n] = c
  freq[heap_n] = count
  left[heap_n] = left_node ? left_node : 0
  right[heap_n] = right_node ? right_node : 0
  leftmost[heap_n] = lm ? lm : c
  sift_up(heap_n)
}

function heap_print(node) {
  printf "heap(%s): %s,%s,%s,%s,%s\n", node, left[node], right[node], char[node], freq[node], leftmost[node]
}

function heap_out_print(node) {
  printf "out(%s): %s,%s,%s,%s,%s\n", node, out_left[node], out_right[node], out_char[node], out_freq[node], out_leftmost[node]
}

function heap_pop(   res) {
  if (!heap_n) return
  res = 1
  if (heap_n == 1) {
    heap_out(1)
    delete left[heap_n]
    delete right[heap_n]
    delete char[heap_n]
    delete freq[heap_n]
    delete leftmost[heap_n]
    heap_n--
    return heap_out_n
  }
  heap_out(1)
  heap_swap(1, heap_n)
  delete left[heap_n]
  delete right[heap_n]
  delete char[heap_n]
  delete freq[heap_n]
  delete leftmost[heap_n]
  heap_n--
  sift_down(1)
  return heap_out_n
}

function merge_and_push(node_a, node_b,   fq, lm) {
  fq = out_freq[node_a] + out_freq[node_b]
  lm = out_leftmost[node_a] < out_leftmost[node_b] ? out_leftmost[node_a] : out_leftmost[node_b]
  if (out_less(node_a, node_b)) {
    heap_push("", fq, node_a, node_b, lm)
  } else {
    heap_push("", fq, node_b, node_a, lm)
  }
}

function build_root() {
  if (!heap_n) return
  if (heap_n == 1) {
    return heap_pop()
  }
  while (heap_n > 1) {
    merge_and_push(heap_pop(), heap_pop())
  }
  return heap_pop()
}

function build_converter(node, prefix) {
  if (out_left[node] == 0 && out_right[node] == 0) {
    print "# out_char[node]:", out_char[node], "prefix:", prefix
    converter[out_char[node]] = prefix
    return
  }
  if (out_left[node]) {
    prefix = prefix "0"
    build_converter(out_left[node], prefix)
  }
  if (out_right[node]) {
    prefix = prefix "1"
    build_converter(out_right[node], prefix)
  }
}

function encode(str,   enc) {
  enc = ""
  for (i = 1; i <= length(str); i++) {
    enc = enc converter[substr(str, i, 1)]
  }
  return enc
}

function decode(enc, root,   dec) {
  cur = root
  dec = ""
  for (i = 1; i <= length(enc); i++) {
    # is terminal
    if (out_left[cur] == 0 && out_right[cur] == 0) {
      dec = dec out_char[cur]
      cur = root
      continue
    }
    dir = substr(enc, i, 1)
    cur = dir == "0" ? out_left[cur] : out_right[cur]
  }
  return dec
}

NR == 1 {
  print $0
  print "==="
  n = length($0)
  for (i = 1; i <= n; i++) {
    c = substr($0, i, 1)
    frequency[c] = frequency[c] ? frequency[c] + 1 : 1
  }
  for (c in frequency) {
    print "c:", c, "frequency: ", frequency[c]
    heap_push(c, frequency[c])
  }

  # for (i = 1; i <= heap_n; i++) {
  #   heap_print(i)
  # }

  root = build_root()
  build_converter(root)

  enc = encode($0)
  print enc
  dec = decode(enc, root)
  print dec


  # for (i = 1; i <= heap_n; i++) {
  #   heap_print(i)
  # }

  # for (i = 1; i <= heap_out_n; i++) {
  #   heap_out_print(i)
  # }

  # while (heap_n) {
  #   heap_pop()
  #   heap_out_print(heap_out_n)
  # }

  # if (heap_n == 1) converter
  # while (heap_n >= 1) {
  # }

}
