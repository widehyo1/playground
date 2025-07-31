#!/bin/bash

# Script to run all GVPR examples and generate output images
# Make sure you have graphviz installed: sudo apt-get install graphviz

echo "Running GVPR Examples Collection"
echo "================================"

# Check if gvpr and dot are available
if ! command -v gvpr &> /dev/null; then
    echo "Error: gvpr not found. Please install graphviz."
    exit 1
fi

if ! command -v dot &> /dev/null; then
    echo "Error: dot not found. Please install graphviz."
    exit 1
fi

# Create output directory
mkdir -p output

echo ""
echo "Example 1: Highlighting Leaf Nodes"
echo "-----------------------------------"
gvpr -f example1_highlight_leaves.gvpr example1_input.dot > output/example1_output.dot
if [ $? -eq 0 ]; then
    dot -Tpng output/example1_output.dot -o output/example1_output.png
    echo "✓ Generated: output/example1_output.png"
else
    echo "✗ Failed to process example 1"
fi

echo ""
echo "Example 2: Extracting Server Infrastructure"
echo "-------------------------------------------"
gvpr -f example2_extract_servers.gvpr example2_network.dot > output/example2_output.dot
if [ $? -eq 0 ]; then
    dot -Tpng output/example2_output.dot -o output/example2_output.png
    echo "✓ Generated: output/example2_output.png"
else
    echo "✗ Failed to process example 2"
fi

echo ""
echo "Example 3: Counting Descendants"
echo "-------------------------------"
gvpr -f example3_count_descendants.gvpr example3_tree.dot > output/example3_output.dot
if [ $? -eq 0 ]; then
    dot -Tpng output/example3_output.dot -o output/example3_output.png
    echo "✓ Generated: output/example3_output.png"
else
    echo "✗ Failed to process example 3"
fi

echo ""
echo "Example 4: Detecting Circular Dependencies"
echo "------------------------------------------"
gvpr -f example4_detect_cycles.gvpr example4_dependencies.dot > output/example4_output.dot
if [ $? -eq 0 ]; then
    dot -Tpng output/example4_output.dot -o output/example4_output.png
    echo "✓ Generated: output/example4_output.png"
else
    echo "✗ Failed to process example 4"
fi

echo ""
echo "Example 5: Simple Filtering (using example1 input)"
echo "---------------------------------------------------"
gvpr -f example5_simple_filter.gvpr example1_input.dot > output/example5_output.dot
if [ $? -eq 0 ]; then
    dot -Tpng output/example5_output.dot -o output/example5_output.png
    echo "✓ Generated: output/example5_output.png"
else
    echo "✗ Failed to process example 5"
fi

echo ""
echo "Also generating original input visualizations for comparison:"
echo "------------------------------------------------------------"

# Generate original input visualizations for comparison
dot -Tpng example1_input.dot -o output/example1_input.png
echo "✓ Generated: output/example1_input.png"

dot -Tpng example2_network.dot -o output/example2_input.png
echo "✓ Generated: output/example2_input.png"

dot -Tpng example3_tree.dot -o output/example3_input.png
echo "✓ Generated: output/example3_input.png"

dot -Tpng example4_dependencies.dot -o output/example4_input.png
echo "✓ Generated: output/example4_input.png"

echo ""
echo "All examples completed! Check the output/ directory for results."
echo "Compare the input and output images to see the transformations."
echo ""
echo "You can also run individual examples manually:"
echo "  gvpr -f example1_highlight_leaves.gvpr example1_input.dot | dot -Tpng -o result.png" 