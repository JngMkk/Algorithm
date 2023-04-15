package Greedy

object greedy01 {
    def main(args: Array[String]): Unit = {
        var N = scala.io.StdIn.readInt()

        var cnt: Int = 0

        val coin: Array[Int] = Array(500, 100, 50, 10)

        for (c <- coin) {
            cnt += N / c
            N %= c
        }

        println(cnt)
    }
}
