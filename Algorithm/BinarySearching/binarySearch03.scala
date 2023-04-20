import java.util.Scanner

object binarySearch03 {
    def getRightIdx(arr: Array[Int], target: Int, start: Int, end: Int): Int = {
        var s = start
        var e = end
        while (s < e) {
            val mid = (s + e) / 2
            if (arr(mid) > target) e = mid
            else s = mid + 1
        }
        s
    }

    def getLeftIdx(arr: Array[Int], target: Int, start: Int, end: Int): Int = {
        var s = start
        var e = end
        while (s < e) {
            val mid = (s + e) / 2
            if (arr(mid) < target) s = mid + 1
            else e = mid
        }
        s
    }

    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val x = sc.nextInt()
        val arr = new Array[Int](n)

        for (i <- 0 until n) {
            arr(i) = sc.nextInt()
        }

        val cnt = getRightIdx(arr, x, 0, n) - getLeftIdx(arr, x, 0, n)
        if (cnt == 0) println(-1)
        else println(cnt)
    }
}
