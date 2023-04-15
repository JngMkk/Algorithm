package BFSAndDFS

object DFS01 {
    def dfs(graph: Array[Array[Int]], v: Int, visited: Array[Boolean]): Unit = {
        visited(v) = true
        printf("%d ", v)
        for (i <- graph(v)) {
            if (!visited(i)) dfs(graph, i, visited)
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

        dfs(graph, 1, visited)
        println()
    }
}
