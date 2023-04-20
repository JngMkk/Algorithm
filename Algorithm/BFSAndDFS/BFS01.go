package main

import "fmt"

type Queue []int

var (
	graph = [9][]int{
		{},
		{2, 3, 8},
		{1, 7},
		{1, 4, 5},
		{3, 5},
		{3, 4},
		{7},
		{2, 6, 8},
		{1, 7},
	}
	visited = [9]bool{}
)

func (q *Queue) enQueue(elem int) {
	*q = append(*q, elem)
}

func (q *Queue) deQueue() int {
	elem := (*q)[0]
	*q = (*q)[1:]
	return elem
}

func (q *Queue) nonEmpty() bool {
	return len(*q) != 0
}

func bfs(queue Queue, start int, visited []bool) {
	queue.enQueue(start)
	visited[start] = true

	for queue.nonEmpty() {
		v := queue.deQueue()
		fmt.Printf("%d ", v)
		for _, i := range graph[v] {
			if !visited[i] {
				queue.enQueue(i)
				visited[i] = true
			}
		}
	}
}

func main() {
	var queue Queue

	bfs(queue, 1, visited[:])
	fmt.Println()
}
