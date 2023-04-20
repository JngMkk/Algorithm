import java.util.Scanner
import scala.util.control.Breaks.{break, breakable}

object sortEx {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val k = sc.nextInt()

        var a = new Array[Int](n)
        var b = new Array[Int](n)

        for (i <- 0 until n) {
            a(i) = sc.nextInt()
        }

        for (i <- 0 until n) {
            b(i) = sc.nextInt()
        }
        a = a.sortWith(_ < _)
        b = b.sortWith(_ > _)

        println(a.mkString(""))
        println(b.mkString(""))

        breakable {
            for (i <- 0 until k) {
                if (a(i) < b(i)) {
                    val temp = a(i)
                    a(i) = b(i)
                    b(i) = temp
                }
                else break
            }
        }
        var res = 0
        for (i <- a.indices) {
            res += a(i)
        }
        println(res)
    }
}
