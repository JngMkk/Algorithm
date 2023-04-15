package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func numAdd(s string) []int {
	var n []int
	for _, f := range strings.Fields(s) {
		i, _ := strconv.Atoi(f)
		n = append(n, i)
	}
	return n
}

func main() {
	var data []int
	sc := bufio.NewScanner(os.Stdin)

	sc.Scan()
	sc.Scan()
	data = numAdd(sc.Text())
	sort.Ints(data)
	inG := 0
	gCnt := 0

	for d := range data {
		inG += 1
		if inG >= d {
			gCnt += 1
			inG = 0
		}
	}

	fmt.Println(gCnt)
}
