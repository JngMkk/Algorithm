package Greedy

import java.util.Scanner
import scala.collection.mutable.ArrayBuffer

object greedy04 {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val data = ArrayBuffer[Int]()

        for (_ <- 0 until n) {
            data += sc.nextInt()
        }
        data.sorted

        var inG = 0
        var gCnt = 0

        for (i <- data) {
            inG += 1
            if (inG >= i) {
                gCnt += 1
                inG = 0
            }
        }

        println(gCnt)
    }
}
