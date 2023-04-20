package Greedy

import java.util.Scanner
import scala.util.control.Breaks

object greedy02 {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)

        var N = sc.nextInt()
        val K = sc.nextInt()
        val loop = new Breaks
        var cnt: Int = 0

        loop.breakable {
            do {
                val target = (N / K) * K
                cnt += N - target
                N = target
                if (N < K) loop.break
                N /= K
                cnt += 1
            } while (true)
        }

        cnt += N - 1
        println(cnt)
    }
}
