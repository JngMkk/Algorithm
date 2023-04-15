package main

import "fmt"

type Stack []interface{}

func (s *Stack) isEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) push(elem interface{}) {
	*s = append(*s, elem)
}

func (s *Stack) pop() interface{} {
	if s.isEmpty() {
		fmt.Println("stack is empty")
		return nil
	} else {
		top := len(*s) - 1
		elem := (*s)[top]
		*s = (*s)[:top]
		return elem
	}
}

func (s *Stack) reverse() Stack {
	var rev Stack
	for i := range *s {
		rev = append(rev, (*s)[len(*s)-i-1])
	}
	return rev
}

func main() {
	// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
	var stack Stack
	stack.push(5)
	stack.push(2)
	stack.push(3)
	stack.push(7)
	stack.pop()
	stack.push(1)
	stack.push(4)
	stack.pop()
	stack.isEmpty()

	fmt.Println(stack)
	fmt.Println(stack.reverse())
}
