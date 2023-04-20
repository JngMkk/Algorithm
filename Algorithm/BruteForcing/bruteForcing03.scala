package BruteForcing

object bruteForcing03 {
    def main(args: Array[String]): Unit = {
        val p = scala.io.StdIn.readLine()
        val row = p(1) - '0'
        val col = p(0) - 'a' + 1

        val dx = Array(-2, -2, -1, -1, 1, 1, 2, 2)
        val dy = Array(-1, 1, -2, 2, -2, 2, -1, 1)

        var cnt = 0

        for (i <- 0 until 8) {
            val nr = row + dx(i)
            val nc = col + dy(i)
            if (nr >= 1 && nc >= 1 && nr <= 8 && nc <= 8) cnt += 1
        }

        println(cnt)
    }
}
