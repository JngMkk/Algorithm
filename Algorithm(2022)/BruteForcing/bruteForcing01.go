package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	n, _ := strconv.Atoi(sc.Text())
	sc.Scan()
	plan := strings.Split(sc.Text(), " ")

	x := 1
	y := 1
	dx := [4]int{0, 0, 1, -1}
	dy := [4]int{1, -1, 0, 0}
	direction := [4]string{"R", "L", "D", "U"}

	for _, p := range plan {
		var nx int = 0
		var ny int = 0
		for i := 0; i < len(direction); i++ {
			if p == direction[i] {
				nx = x + dx[i]
				ny = y + dy[i]
			}
		}
		if nx < 1 || ny < 1 || nx > n || ny > n {
			continue
		}
		x = nx
		y = ny
	}
	fmt.Println(x, y)
}
