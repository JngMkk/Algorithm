package main

import "fmt"

func dfs(graph [][]int, v int, visited []bool) {
	visited[v] = true
	fmt.Printf("%d ", v)
	for _, i := range graph[v] {
		if !(visited[i]) {
			dfs(graph, i, visited)
		}
	}
}

func main() {
	visited := [9]bool{}
	graph := [9][]int{
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

	dfs(graph[:], 1, visited[:])
	fmt.Println()
}
