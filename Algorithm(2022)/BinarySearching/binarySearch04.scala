/*
문제

    사용자는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했음. 오늘은 떡볶이 떡을 만드는 날.
    사용자의 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않음.
    대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줌.

    절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단함.
    높이 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않음.

    예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15가 될 것.
    잘린 떡의 길이는 차례대로 4, 0, 0, 2cm임. 손님은 6cm만큼의 길이를 가져감.

    손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램 작성.

    첫 줄에 떡의 개수와 M.

    입력 예시
    4 6
    19 15 10 17
*/

import java.util.Scanner

object binarySearch04 {
    def main(args: Array[String]): Unit = {
        val sc = new Scanner(System.in)
        val n = sc.nextInt()
        val m = sc.nextInt()
        val arr = new Array[Int](n)
        for (i <- 0 until n) {
            arr(i) = sc.nextInt()
        }
        var start = 0
        var end = arr.max
        var res = 0

        while (start < end) {
            var total = 0
            val mid = (start + end) / 2

            for (x <- arr) {
                if (x > mid) total += x - mid
            }

            if (total >= m) {
                res = mid
                start += 1
            } else {
                end = mid
            }
        }
        println(res)
    }
}
