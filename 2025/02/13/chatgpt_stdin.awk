# myscript.awk
{
    # Read the next line from file "file.txt"
    getline line

    # Print the current line and the next line read from file.txt
    print "Current line:", $0
    print "Next line from candidates.txt:", line
}
