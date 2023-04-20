package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var (
	a []int
	b []int
)

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Scan()
	str := strings.Split(sc.Text(), " ")
	k, _ := strconv.Atoi(str[1])
	sc.Scan()
	for i, v := range sc.Text() {
		if i%2 == 0 {
			a = append(a, int(v-'0'))
		}
	}
	sc.Scan()
	for i, v := range sc.Text() {
		if i%2 == 0 {
			b = append(b, int(v-'0'))
		}
	}
	sort.Slice(a, func(i, j int) bool {
		return a[i] < a[j]
	})
	sort.Slice(b, func(i, j int) bool {
		return b[j] < b[i]
	})

	for i := 0; i < k; i++ {
		if a[i] < b[i] {
			a[i], b[i] = b[i], a[i]
		} else {
			break
		}
	}

	sum := 0

	for i := 0; i < len(a); i++ {
		sum += a[i]
	}
	fmt.Println(sum)
}
