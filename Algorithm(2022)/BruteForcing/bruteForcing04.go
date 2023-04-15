package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
)

func sumInt(nums ...int) int {
	res := 0
	for _, n := range nums {
		res += n
	}
	return res
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var str string
	fmt.Fscanln(reader, &str)

	var al []string
	var num []int

	for _, s := range str {
		if unicode.IsDigit(s) {
			n, _ := strconv.Atoi(string(s))
			num = append(num, n)
		} else {
			al = append(al, string(s))
		}
	}
	sort.Strings(al)
	fmt.Println(strings.Join(al, "") + strconv.Itoa(sumInt(num...)))
}
