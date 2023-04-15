/*
문제

	사용자는 N X M 크기의 직사각형 형태의 미로에 갇힘. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 함.

	사용자의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있음.
	이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있음. 미로는 반드시 탈출할 수 있는 형태로 제시됨.

	이때 사용자가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산함.

	입력 예시
	5 6
	101010
	111111
	000001
	111111
	111111
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type myQueue []Tuple

type Tuple struct {
	first  int
	second int
}

var (
	dx        = []int{-1, 1, 0, 0}
	dy        = []int{0, 0, -1, 1}
	mazeGraph [][]int
	n         int
	m         int
)

func (q *myQueue) enQueue(t Tuple) {
	*q = append(*q, t)
}

func (q *myQueue) deQueue() Tuple {
	if !q.nonEmpty() {
		fmt.Println("queue is empty")
	}
	ret := (*q)[0]
	*q = (*q)[1:]
	return ret
}

func (q *myQueue) nonEmpty() bool {
	return len(*q) != 0
}

func mazeBFS(q myQueue, x, y int) int {
	q.enQueue(Tuple{x, y})

	for q.nonEmpty() {
		output := q.deQueue()
		x := output.first
		y := output.second
		for i := 0; i < 4; i++ {
			nx := x + dx[i]
			ny := y + dy[i]
			if nx <= -1 || nx >= n || ny <= -1 || ny >= m {
				continue
			}
			if mazeGraph[nx][ny] == 0 {
				continue
			}
			if mazeGraph[nx][ny] == 1 {
				q.enQueue(Tuple{nx, ny})
				mazeGraph[nx][ny] = mazeGraph[x][y] + 1
			}
		}
	}
	return mazeGraph[n-1][m-1]
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()

	n, _ = strconv.Atoi(strings.Split(sc.Text(), " ")[0])
	m, _ = strconv.Atoi(strings.Split(sc.Text(), " ")[1])

	var q myQueue

	for i := 0; i < n; i++ {
		var ints []int
		sc.Scan()
		var str = sc.Text()
		for j := 0; j < len(str); j++ {
			num := int(str[j] - '0')
			ints = append(ints, num)
		}
		mazeGraph = append(mazeGraph, ints)
	}
	fmt.Println(mazeBFS(q, 0, 0))
}
