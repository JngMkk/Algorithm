package main

import "fmt"

var arr = []int{2, 7, 11, 15}

const target int = 9

func two_sum(nums []int, target int) []int {
	numsMap := make(map[int]int)

	for i, num := range nums {
		numsMap[num] = i
	}

	for i, num := range nums {
		if j, ok := numsMap[target-num]; ok && i != j {
			return []int{i, j}
		}
	}

	return []int{}
}

func main() {
	fmt.Println(two_sum(arr, target))
}
