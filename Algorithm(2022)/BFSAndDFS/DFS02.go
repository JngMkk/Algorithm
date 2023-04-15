package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	DFSgraph [][]int
	k, l     int
)

func icecreamDFS(x, y int) bool {
	if x <= -1 || x >= k || y <= -1 || y >= l {
		return false
	}

	if DFSgraph[x][y] == 0 {
		DFSgraph[x][y] = 1
		icecreamDFS(x-1, y)
		icecreamDFS(x+1, y)
		icecreamDFS(x, y-1)
		icecreamDFS(x, y+1)
		return true
	}
	return false
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	k, _ = strconv.Atoi(strings.Split(sc.Text(), " ")[0])
	l, _ = strconv.Atoi(strings.Split(sc.Text(), " ")[1])

	for i := 0; i < k; i++ {
		var ints []int
		sc.Scan()
		var str = sc.Text()
		for j := 0; j < len(str); j++ {
			num := int(str[j] - '0')
			ints = append(ints, num)
		}
		DFSgraph = append(DFSgraph, ints)
	}

	var res int

	for i := 0; i < k; i++ {
		for j := 0; j < l; j++ {
			if icecreamDFS(i, j) {
				res += 1
			}
		}
	}
	fmt.Println(res)
}
