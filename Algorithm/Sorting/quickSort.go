package main

import "fmt"

func quickSort(array *[]int, start, end int) {
	if start >= end {
		return
	}
	left := start + 1
	right := end
	pivot := start

	for left <= right {
		for left <= end && (*array)[left] <= (*array)[pivot] {
			left++
		}
		for right > start && (*array)[right] >= (*array)[pivot] {
			right--
		}
		if left > right {
			(*array)[right], (*array)[pivot] = (*array)[pivot], (*array)[right]
		} else {
			(*array)[left], (*array)[right] = (*array)[right], (*array)[left]
		}
	}

	quickSort(array, start, right-1)
	quickSort(array, right+1, end)
}

func main() {
	arr := []int{7, 5, 9, 0, 3, 1, 6, 2, 4, 8}
	quickSort(&arr, 0, len(arr)-1)
	for _, v := range arr {
		fmt.Printf("%d ", v)
	}
	fmt.Println()
}
