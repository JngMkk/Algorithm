package Greedy

object greedy03 {
    def main(args: Array[String]): Unit = {
        val s = scala.io.StdIn.readLine()
        var res = s(0) - '0'

        for (i <- 1 until s.length) {
            val n = s(i) - '0'
            if (res < 2 || n < 2) {
                res += n
            } else {
                res *= n
            }
        }

        println(res)
    }
}
