object quickSort {

    def quickSort(array: Array[Int], start: Int, end: Int): Unit = {
        if (start >= end) { return }

        var left = start + 1
        var right = end
        val pivot = start

        while (left <= right) {
            while (left <= end && array(left) <= array(pivot)) left += 1
            while (right > start && array(right) >= array(pivot)) right -= 1
            if (left > right) {
                val temp = array(pivot)
                array(pivot) = array(right)
                array(right) = temp
            }
            else {
                val temp = array(left)
                array(left) = array(right)
                array(right) = temp
            }
        }
        quickSort(array, start, right-1)
        quickSort(array, right+1, end)
    }

    def main(args: Array[String]): Unit = {
        val arr = Array(7, 5, 9, 0, 3, 1, 6, 2, 4, 8)
        quickSort(arr, 0, arr.length - 1)
        println(arr.mkString(" "))
    }
}
