
class Direction (var value: Int) {
    // class for representing direction
    // 0b001: up      direction string representation is "↑"
    // 0b010: left    direction string representation is "←"
    // 0b100: upleft  direction string representation is "↖"
    // 0b000: default direction string representation is "-"
    // hence each direction can coexist,
    // direction info is stored in value, which is interpreted bitwise

    override fun toString(): String {
        if (this.value == 0b000) return "-"
        var reprList: MutableList<String> = mutableListOf()
        if (this.value and 0b001 != 0) reprList.add("↑")
        if (this.value and 0b010 != 0) reprList.add("←")
        if (this.value and 0b100 != 0) reprList.add("↖")

        return reprList.joinToString("|")
    }

}

data class Tuple(val row: Int, val col: Int, val resultX: String, val resultY: String)

fun smithWaterman(
    x: String,
    y: String,
): String {
    val tx: String = " $x"
    val ty: String = " $y"
    var matrix: Array<Array<Pair<Int, Direction>>> = Array(tx.length) {Array(ty.length) { 0 to Direction(0b000) } }
    var score: Int = 0
    var positionCandidateList: MutableList<Pair<Int, Int>> = mutableListOf()

    // helper function
    fun calcElementValue(
        row: Int,
        col: Int,
        match: Int = 3,
        misMatch: Int = -3,
        gapPanalty: Int = -2,
    ): Int {
        // a closure function to calculate each element with free variables:
        // matrix, tx, ty, (highest) score, positionCandidateList
        require(row > 0) { "Invalid row index($row) found" }
        require(col > 0) { "Invalid column index($col) found" }

        val (upValue, upDirection) = matrix[row-1][col]
        val (leftValue, leftDirection) = matrix[row][col-1]
        val (diagValue, diagDirection) = matrix[row-1][col-1]

        val upCandidate = upValue + gapPanalty
        val leftCandidate = leftValue + gapPanalty
        var diagCandidate = diagValue + misMatch
        if (tx[row] == ty[col]) {
            diagCandidate = diagValue + match
        }

        val elementValue = maxOf(upCandidate, leftCandidate, diagCandidate)
        if (elementValue < 0) {
            matrix[row][col] = 0 to Direction(0b000)
            return score
        }

        var elementDirection = Direction(0b000)

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

        if (elementValue > score) {
            positionCandidateList.clear()
            positionCandidateList.add(row to col)
            return elementValue
        }
        if (elementValue == score) {
            positionCandidateList.add(row to col)
            return elementValue
        }
        return score
    }

    // init phase
    for (i in matrix.indices) {
        for (j in matrix[i].indices) {
            if (i == 0 || j == 0) continue
            score = calcElementValue(i, j)
        }
    }

    visualizeMatrix(tx, ty, matrix)

    if (positionCandidateList.size == 0) {
        return ""
    }

    var stack = ArrayDeque<Tuple>()
    var resultList: MutableList<Pair<String, String>> = mutableListOf()

    for (pair in positionCandidateList) {
        val (candidateRow, candidateCol) = pair
        stack.add(Tuple(candidateRow, candidateCol, "", ""))
    }

    while (stack.size > 0) {
        val curEle = stack.removeLast()
        val curRow = curEle.row
        val curCol = curEle.col
        val curResultX = curEle.resultX
        val curResultY = curEle.resultY

        val (curValue, curDirection) = matrix[curRow][curCol]

        // base condition
        if (curValue == 0) {
            resultList.add(curResultX to curResultY)

            // find the first result and exit
            break
        }

        if (curDirection.value and 0b001 != 0) {
            stack.add(Tuple(curRow - 1, curCol, "-" + curResultX, curResultY))
        }
        if (curDirection.value and 0b010 != 0) {
            stack.add(Tuple(curRow, curCol - 1, curResultX, "-" + curResultY))
        }
        if (curDirection.value and 0b100 != 0) {
            stack.add(Tuple(curRow - 1, curCol - 1, tx[curRow] + curResultX, ty[curCol] + curResultY))
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
    val x = "GGTTGACTA"
    val y = "TGTTACGG"
    val res = smithWaterman(x, y)
    println(res)
}
