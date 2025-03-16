enum class Direction {
    DEFAULT,
    UP,
    LEFT,
    UPLEFT,
    UPANDLEFT,
    ;

    companion object {
        val representation =
            mapOf(
                DEFAULT to "-",
                UP to "↑",
                LEFT to "←",
                UPLEFT to "↖",
                UPANDLEFT to "⬑",
            )
    }

    override fun toString(): String = representation[this] ?: super.toString()
}

fun longestCommonSubsequence(
    x: String,
    y: String,
): String {
    // Matrix to store pair of Int and Direction
    val matrix: Array<Array<Pair<Int, Direction>>> = Array(x.length + 1) { Array(y.length + 1) { 0 to Direction.DEFAULT } }

    fun calcElementValue(
        row: Int,
        col: Int,
    ): Pair<Int, Direction> {
        require(row > 0) { "Invalid row index($row) found" }
        require(col > 0) { "Invalid column index($col) found" }

        if (x[row - 1] == y[col - 1]) {
            val (value, direction) = matrix[row - 1][col - 1]
            matrix[row][col] = value + 1 to Direction.UPLEFT
        } else {
            val (leftValue, _) = matrix[row][col - 1]
            val (upValue, _) = matrix[row - 1][col]
            if (leftValue > upValue) {
                matrix[row][col] = leftValue to Direction.LEFT
            } else if (leftValue < upValue) {
                matrix[row][col] = upValue to Direction.UP
            } else {
                matrix[row][col] = upValue to Direction.UPANDLEFT
            }
        }
        return matrix[row][col]
    }

    if (x.isEmpty() || y.isEmpty()) return ""

    val tx = " $x"
    val ty = " $y"
    val rowCnt = tx.length
    val colCnt = ty.length

    for (ix in 1 until rowCnt) {
        for (iy in 1 until colCnt) {
            calcElementValue(ix, iy)
        }
    }

    visualizedMatrix(tx, ty, matrix)

    var curRow = rowCnt - 1
    var curCol = colCnt - 1

    var result = ""
    while (curRow > 0 && curCol > 0) {
        val (curValue, curDirection) = matrix[curRow][curCol]
        when (curDirection) {
            Direction.UP, Direction.UPANDLEFT -> curRow--
            Direction.LEFT -> curCol--
            Direction.UPLEFT -> {
                result = tx[curRow] + result
                curRow--
                curCol--
            }
            Direction.DEFAULT -> {
                println("Error")
                break
            }
        }
    }
    return result
}

fun visualizedMatrix(
    tx: String,
    ty: String,
    matrix: Array<Array<Pair<Int, Direction>>>,
) {
    println("•|${ty.toList().joinToString("|")}")
    for (idx in matrix.indices) {
        val row = matrix[idx].joinToString("|") { "${it.first}${it.second}" }
        println("${tx[idx]}|$row")
    }
}

fun main() {
    val x = "XMJYAUZ"
    val y = "MZJAWXU"
    val lcs = longestCommonSubsequence(x, y)
    println(lcs) // Expected output: Q
}
