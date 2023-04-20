package BruteForcing

import java.util.Scanner
import scala.util.control.Breaks.{breakable, break}

object bruteForcing01 {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        sc.nextLine()
        val plan = sc.nextLine().split(" ")
        var x, y = 1

        val dx = Array(0, 0, 1, -1)
        val dy = Array(1, -1, 0, 0)
        val direction = Array("R", "L", "D", "U")

        for (p <- plan) {
            breakable {
                var nx, ny = 0
                for (i <- direction.indices) {
                    if (p == direction(i)) {
                        nx = x + dx(i)
                        ny = y + dy(i)
                    }
                }
                if (nx < 1 || ny < 1 || nx > n || ny > n) break
                x = nx
                y = ny
            }
        }

        println(x, y)
    }
}
