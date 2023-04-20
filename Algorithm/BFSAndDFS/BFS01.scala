package BFSAndDFS

import scala.collection.mutable

object BFS01 {
    def bfs(graph: Array[Array[Int]], start: Int, visited: Array[Boolean]): Unit = {
        val queue = mutable.Queue[Int]()
        queue.enqueue(start)
        visited(start) = true

        while (queue.nonEmpty) {
            val v = queue.dequeue()
            printf("%d ", v)
            for (i <- graph(v)) {
                if (!visited(i)) {
                    queue.enqueue(i)
                    visited(i) = true
                }
            }
        }
    }

    def main(args: Array[String]): Unit = {
        val graph = Array(
            Array(0),
            Array(2, 3, 8),
            Array(1, 7),
            Array(1, 4, 5),
            Array(3, 5),
            Array(3, 4),
            Array(7),
            Array(2, 6, 8),
            Array(1, 7)
        )
        var visited = Array.ofDim[Boolean](9)

        bfs(graph, 1, visited)
        println()
    }
}
