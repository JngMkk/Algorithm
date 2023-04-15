package BruteForcing

object bruteForcing02 {
    def check(h: Int, m: Int, s: Int): Boolean = {
        if (h % 10 == 3 || m / 10 == 3 || m % 10 == 3 || s / 10 == 3 || s % 10 == 3) true
        else false
    }
    def main(args: Array[String]): Unit = {
        val n = scala.io.StdIn.readInt()
        var cnt = 0
        var cnt2 = 0

        for (h <- 0 to n) {
            for (m <- 0 until 60) {
                for (s <- 0 until 60) {
                    val time = h.toString + m.toString + s.toString
                    if (time.contains("3")) cnt += 1
                    if (check(h, m, s)) cnt2 += 1
                }
            }
        }

        println(cnt, cnt2)
    }
}
