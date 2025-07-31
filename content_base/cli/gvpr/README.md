# GVPR Examples Collection

This collection provides practical examples of using GVPR (Graph Processing Language) with Graphviz. GVPR is a powerful language for processing and transforming graph structures that comes bundled with Graphviz.

## What is GVPR?

GVPR (Graph Processing Language) is a domain-specific language designed for processing graphs. It allows you to:

- Filter and transform graph structures
- Modify node and edge attributes
- Extract subgraphs based on criteria
- Analyze graph properties (cycles, paths, connectivity)
- Generate reports and statistics about graphs

## Installation

GVPR comes with Graphviz. To install Graphviz:

**On Ubuntu/Debian:**
```bash
sudo apt-get install graphviz
```

**On CentOS/RHEL:**
```bash
sudo yum install graphviz
```

**On macOS:**
```bash
brew install graphviz
```

**On Windows:**
Download from [Graphviz website](https://graphviz.org/download/)

## Basic Usage

```bash
# Process a graph with a gvpr program
gvpr -f program.gvpr input.dot > output.dot

# Process and render directly
gvpr -f program.gvpr input.dot | dot -Tpng -o output.png

# With command line arguments
gvpr -f program.gvpr -a "arg1" -a "arg2" input.dot
```

## Examples in this Collection

### Example 1: Highlight Leaf Nodes
**Files:** `example1_input.dot`, `example1_highlight_leaves.gvpr`

Demonstrates basic node filtering and styling. Highlights employees with no subordinates (leaf nodes) in an organizational chart.

```bash
# Run the example
gvpr -f example1_highlight_leaves.gvpr example1_input.dot > output1.dot
dot -Tpng output1.dot -o output1.png
```

**Key concepts:**
- Node degree checking (`outdegree()`)
- Basic styling (`color`, `fillcolor`, `style`)
- Conditional processing

### Example 2: Extract Server Infrastructure
**Files:** `example2_network.dot`, `example2_extract_servers.gvpr`

Shows how to extract specific subgraphs based on node types. Creates a new graph containing only servers and their immediate connections.

```bash
# Run the example
gvpr -f example2_extract_servers.gvpr example2_network.dot > server_network.dot
dot -Tpng server_network.dot -o server_network.png
```

**Key concepts:**
- Graph creation (`graph()`)
- Node cloning (`clone()`)
- Attribute-based filtering
- Multi-pass processing

### Example 3: Count Descendants
**Files:** `example3_tree.dot`, `example3_count_descendants.gvpr`

Demonstrates tree traversal and counting. Counts descendants for each node and updates labels accordingly.

```bash
# Run the example
gvpr -f example3_count_descendants.gvpr example3_tree.dot > counted_tree.dot
dot -Tpng counted_tree.dot -o counted_tree.png
```

**Key concepts:**
- Tree/graph traversal
- Non-recursive algorithms (GVPR limitation)
- Label modification (`sprintf()`)
- Custom functions

### Example 4: Detect Circular Dependencies
**Files:** `example4_dependencies.dot`, `example4_detect_cycles.gvpr`

Advanced example showing cycle detection in dependency graphs. Highlights nodes and edges involved in circular dependencies.

```bash
# Run the example
gvpr -f example4_detect_cycles.gvpr example4_dependencies.dot > analyzed_deps.dot
dot -Tpng analyzed_deps.dot -o analyzed_deps.png
```

**Key concepts:**
- Cycle detection algorithms
- Path finding
- Complex multi-pass processing
- Edge styling

### Example 5: Simple Filtering
**Files:** `example5_simple_filter.gvpr` (works with any .dot file)

Basic example showing pattern matching and attribute modification.

```bash
# Run with any input file
gvpr -f example5_simple_filter.gvpr example1_input.dot > filtered_output.dot
```

**Key concepts:**
- Pattern matching (`match()`)
- String functions (`toupper()`)
- Regular expressions
- Basic transformations

## GVPR Language Basics

### Structure
```gvpr
BEGIN { 
    // Initialization code
}

BEG_G { 
    // Per-graph initialization
}

N { 
    // Process each node
}

E { 
    // Process each edge  
}

END_G { 
    // Per-graph cleanup
}

END { 
    // Final cleanup
}
```

### Key Built-in Functions

**Node functions:**
- `fstnode(g)` - first node in graph
- `nxtnode(n)` - next node after n
- `indegree(n)` - number of incoming edges
- `outdegree(n)` - number of outgoing edges

**Edge functions:**
- `fstout(n)` - first outgoing edge from node n
- `nxtout(e)` - next outgoing edge
- `fstin(n)` - first incoming edge to node n
- `nxtin(e)` - next incoming edge

**String functions:**
- `sprintf(format, ...)` - formatted string
- `match(string, pattern)` - regex matching
- `toupper(string)` - uppercase conversion

**Graph functions:**
- `graph(name, type)` - create new graph
- `clone(graph, object)` - clone node/edge to graph

### Variables
- `$` - current object (node or edge)
- `G` - current graph
- `ARGC`, `ARGV[]` - command line arguments
- `$O` - output graph (set in END_G)

## Tips and Limitations

### Tips:
1. **Multiple passes**: Use multiple N{} or E{} blocks for complex processing
2. **Debugging**: Use `printf()` statements to trace execution
3. **Testing**: Start with simple transformations and build complexity
4. **Performance**: GVPR is interpreted, so keep algorithms simple

### Limitations:
1. **No recursion**: Functions cannot call themselves
2. **Limited data structures**: Basic arrays only
3. **No dynamic memory**: Fixed-size arrays
4. **Context sensitivity**: Function calls may overwrite context

## Advanced Usage

### Command Line Arguments
```bash
gvpr -f script.gvpr -a "node_name" -a "max_depth" input.dot
```

Access in GVPR:
```gvpr
BEGIN {
    if (ARGC != 2) {
        print("Usage: script.gvpr node_name max_depth");
        exit(1);
    }
    string target_node = ARGV[0];
    int max_depth = atoi(ARGV[1]);
}
```

### Conditional Processing
```gvpr
N [color == "red"] {
    // Only process red nodes
}

E [$.tail.name == "start"] {
    // Only process edges from "start" node
}
```

### Creating Complex Filters
```gvpr
// Multi-criteria filtering
N [(outdegree($) > 2) && ($.type == "server")] {
    $.color = "important";
}
```

## Further Reading

- [GVPR Manual](https://graphviz.org/pdf/gvpr.3.pdf)
- [Graphviz Documentation](https://graphviz.org/documentation/)
- [DOT Language Reference](https://graphviz.org/doc/info/lang.html)

## Contributing

Feel free to add more examples or improve existing ones. When adding examples:

1. Create both input (.dot) and program (.gvpr) files
2. Add clear comments explaining the logic
3. Update this README with usage instructions
4. Include a brief description of key concepts demonstrated 