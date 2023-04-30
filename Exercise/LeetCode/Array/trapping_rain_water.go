package main

import "fmt"

type Stack []int

func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) push(elem int) {
	*s = append(*s, elem)
}

func (s *Stack) pop() int {
	top := len(*s) - 1
	elem := (*s)[top]
	*s = (*s)[:top]
	return elem
}

func min(x, y int) int {
	if x >= y {
		return y
	} else {
		return x
	}
}

func using_stack(array []int) int {
	var stack Stack
	volume := 0

	for i := 0; i < len(array); i++ {
		for !stack.isEmpty() && array[i] > array[stack[len(stack)-1]] {
			top := stack.pop()

			if stack.isEmpty() {
				break
			}

			distance := i - stack[len(stack)-1] - 1
			waters := min(array[i], array[stack[len(stack)-1]]) - array[top]

			volume += distance * waters
		}
		stack.push(i)
	}

	return volume
}

func main() {
	fmt.Println(using_stack([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
}
