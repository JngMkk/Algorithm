package BFSAndDFS

import java.util.Scanner
import scala.collection.mutable
import scala.util.control.Breaks.{breakable, break}

object BFS02 {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val m = sc.nextInt()
        sc.nextLine()

        val graph = Array.ofDim[Int](n, m)

        for (i <- 0 until n) {
            val str = sc.nextLine()
            for (j <- 0 until str.length) {
                graph(i)(j) = str(j) - '0'
            }
        }

        val dx = Array(-1, 1, 0, 0)
        val dy = Array(0, 0, -1, 1)

        def bfs(x: Int, y: Int): Int = {
            val queue = mutable.Queue[(Int, Int)]()
            queue.enqueue((x, y))

            while (queue.nonEmpty) {
                val (x, y) = queue.dequeue()
                for (i <- 0 until 4) {
                    breakable {
                        val nx = x + dx(i)
                        val ny = y + dy(i)
                        if (nx <= -1 || nx >= n || ny <= -1 || ny >= m) {
                            break
                        }
                        if (graph(nx)(ny) == 0) {
                            break
                        }
                        if (graph(nx)(ny) ==1) {
                            queue.enqueue((nx, ny))
                            graph(nx)(ny) = graph(x)(y) + 1
                        }
                    }
                }
            }
            return graph(n-1)(m-1)
        }
        println(bfs(0, 0))
    }
}
