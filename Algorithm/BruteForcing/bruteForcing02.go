package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(h, m, s int) bool {
	// '시'는 10의 자리 수가 3이 될 수 없으므로 나머지 연산만 함
	if h%10 == 3 || m/10 == 3 || m%10 == 3 || s/10 == 3 || s%10 == 3 {
		return true
	}
	return false
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	cnt := 0
	cnt2 := 0

	// 문자열로 풀 수도 있고 함수 정의해서 풀 수도 있음.
	for h := 0; h <= n; h++ {
		for m := 0; m < 60; m++ {
			for s := 0; s < 60; s++ {
				var time string = strconv.Itoa(h) + strconv.Itoa(m) + strconv.Itoa(s)
				if strings.Contains(time, "3") {
					cnt++
				}
				if check(h, m, s) {
					cnt2++
				}
			}
		}
	}
	fmt.Println(cnt, cnt2)
}
