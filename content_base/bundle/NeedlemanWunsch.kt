class Direction(
    var value: Int,
) {
    override fun toString(): String {
        if (this.value == 0b000) return "-"
        val reprList: MutableList<String> = mutableListOf()
        if (this.value and 0b001 != 0) reprList.add("↑")
        if (this.value and 0b010 != 0) reprList.add("←")
        if (this.value and 0b100 != 0) reprList.add("↖")
        return reprList.joinToString("|")
    }
}

data class Tuple(val row: Int, val col: Int, val xRes: String, val yRes: String)

fun needlemanWunsch(
    x: String,
    y: String,
): String {
    val matrix: Array<Array<Pair<Int, Direction>>> = Array(x.length + 1) { Array(y.length + 1) { 0 to Direction(0b000) } }
    val tx: String = " $x"
    val ty: String = " $y"

    fun calcElementValue(
        row: Int,
        col: Int,
        matchValue: Int = 1,
        misMatchValue: Int = -1,
        gapPanalty: Int = -1,
    ): Pair<Int, Direction> {
        // closure for calculate matrix with free variables:
        // matrix, tx, ty
        require(row > 0) { "Invalid row index($row) found" }
        require(col > 0) { "Invalid column index($col) found" }

        val (upValue, upDirection) = matrix[row - 1][col]
        val (leftValue, leftDirection) = matrix[row][col - 1]
        val (diagValue, diagDirection) = matrix[row - 1][col - 1]

        val upCandidate = upValue + gapPanalty
        val leftCandidate = leftValue + gapPanalty

        var diagCandidate = diagValue + misMatchValue
        if (tx[row] == ty[col]) {
            diagCandidate = diagValue + matchValue
        }

        var elementDirection: Direction = Direction(0b000)

        val elementValue: Int = maxOf(upCandidate, leftCandidate, diagCandidate)
        if (upCandidate == elementValue) {
            elementDirection.value = elementDirection.value or 0b001
        }
        if (leftCandidate == elementValue) {
            elementDirection.value = elementDirection.value or 0b010
        }
        if (diagCandidate == elementValue) {
            elementDirection.value = elementDirection.value or 0b100
        }

        matrix[row][col] = elementValue to elementDirection
        return matrix[row][col]
    }

    // initialize first column
    for (i in matrix.indices) {
        matrix[i][0] = -i to Direction(0b000)
    }
    // initialize first row
    for (j in matrix[0].indices) {
        matrix[0][j] = -j to Direction(0b000)
    }

    for (i in matrix.indices) {
        for (j in matrix[i].indices) {
            if (i == 0 || j == 0) continue
            calcElementValue(i, j)
        }
    }

    visualizeMatrix(tx, ty, matrix)

    var curRow = x.length
    var curCol = y.length
    var xResult = ""
    var yResult = ""

    var stack = ArrayDeque<Tuple>()
    stack.add(Tuple(curRow, curCol, xResult, yResult))

    val resultList: MutableList<Pair<String, String>> = mutableListOf()

    while (stack.size > 0) {
        val curEle = stack.removeLast()
        curRow = curEle.row
        curCol = curEle.col
        xResult = curEle.xRes
        yResult = curEle.yRes

        if (curRow == 0) {
            yResult = "-".repeat(curCol) + yResult
            resultList.add(xResult to yResult)
            if (stack.size > 0) {
                stack.removeLast()
            }
            continue
        }

        if (curCol == 0) {
            xResult = "-" .repeat(curRow) + xResult
            resultList.add(xResult to yResult)
            if (stack.size > 0) {
                stack.removeLast()
            }
            continue
        }

        val (curValue, curDirection) = matrix[curRow][curCol]
        if (curDirection.value and 0b001 != 0) {
            stack.add(Tuple(curRow - 1, curCol, "-" + xResult, yResult))
        }
        if (curDirection.value and 0b010 != 0) {
            stack.add(Tuple(curRow, curCol - 1, xResult, "-" + yResult))
        }
        if (curDirection.value and 0b100 != 0) {
            xResult = tx[curRow] + xResult
            yResult = ty[curCol] + yResult
            stack.add(Tuple(curRow - 1, curCol - 1, xResult, yResult))
        }
    }

    return resultList.joinToString("|")
}

fun visualizeMatrix(
    tx: String,
    ty: String,
    matrix: Array<Array<Pair<Int, Direction>>>,
) {
    println("•|${ty.toList().joinToString("          |")}")
    for (idx in matrix.indices) {
        val rowRepr = matrix[idx].joinToString("|") { "(${ "%+03d".format(it.first) },${ "%5s".format(it.second) })" }
        println("${tx[idx]}|$rowRepr")
    }
}

fun main() {

    // val x = "XMJYAUZ"
    // val y = "MZJAWXU"
    val x = "Reading out a LCS"
    val y = "Reading out all LCSs"
    val res = needlemanWunsch(x, y)
    println(res)
}
