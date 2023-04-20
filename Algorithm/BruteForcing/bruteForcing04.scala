package BruteForcing

import scala.collection.mutable.ArrayBuffer

object bruteForcing04 {
    def main(args: Array[String]): Unit = {
        val str = scala.io.StdIn.readLine()
        val al = ArrayBuffer[String]()
        val num = ArrayBuffer[Int]()

        for (s <- str) {
            if (s.isDigit) num += s - '0'
            else al += s.toString
        }

        println(al.sorted.mkString + num.sum.toString)
    }
}
