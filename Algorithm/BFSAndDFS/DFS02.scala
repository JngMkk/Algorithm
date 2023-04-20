package BFSAndDFS

import java.util.Scanner

object DFS02 {
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

        def dfs(x: Int, y: Int): Boolean = {
            if (x <= -1 || x >= n || y <= -1 || y >= m) return false

            if (graph(x)(y) == 0) {
                graph(x)(y) = 1
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
                return true
            }
            false
        }

        var res = 0

        for (i <- 0 until n) {
            for (j <- 0 until m) {
                if (dfs(i, j)) res += 1
            }
        }
        println(res)
    }
}
