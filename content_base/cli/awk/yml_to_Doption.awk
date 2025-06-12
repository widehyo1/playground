function join(arr, sep, acc) {
    for (idx in arr) {
        acc = acc sep arr[idx]
    }
    return substr(acc, 1 + length(sep))
}

function rstrip(str) {
    gsub(/\s+$/, "", str)
    return str
}

function processLine(str) {
    gsub(/#.*/, "", str)
    str = rstrip(str)
    return str
}

function isPropertyLine(line) {
  return index(line, ":") != length(line)
}

function getIndexLevel(line, indentWidth) {
    return int(index(line, $1) / indentWidth)
}

function getPropertyName(line, indentWidth) {
    return substr(line, getIndexLevel(line, indentWidth) * indentWidth + 1, length($1) - 1)
}

function getPropertyValue(line) {
    return substr(line, index(line, $2))
}

function printProperty(stack, line, indentWidth) {
    print "-D" join(stack, ".") "=" getPropertyValue(line) " \\"
}


function printArr(arr) {
    printf "["
    for (idx in arr) {
        printf arr[idx] ", "
    }
    print "]"
}

function push(stack, item) {
    stackLen++
    stack[stackLen] = item
}

function pop(stack) {
    delete stack[stackLen]
    stackLen--
}

function popUntil(stack, line, indentWidth) {
    indentLevel = getIndexLevel(line, indentWidth)
    while (indentLevel < stackLen) {
        pop(stack)
    }
}

function update(stack, line, indentWidth, item) {
    popUntil(stack, line, indentWidth)
    stack[stackLen] = item
}

BEGIN {
  indentWidth = 2
  split("", stack, "")
  stackLen = 0
}

# skip commented lines
substr($1,1,1) == "#" {
    next
}

# skip empty lines
/^$/ {
    next
}

# process valid lines
{
    line = processLine($0)

    if (getIndexLevel(line, indentWidth) > stackLen) {
        push(stack, getPropertyName(line, indentWidth))
    } else {
        update(stack, line, indentWidth, getPropertyName(line, indentWidth))
    }
    if (isPropertyLine(line)) {
        printProperty(stack, line, indentWidth)
    }
}
