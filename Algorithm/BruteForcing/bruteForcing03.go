package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var p string
	fmt.Fscanln(reader, &p)

	row := int(p[1] - '0')
	col := int(p[0] - 'a' + 1)

	var dx = [8]int{-2, -2, -1, -1, 1, 1, 2, 2}
	var dy = [8]int{1, -1, 2, -2, -2, 2, -1, 1}

	cnt := 0

	for i := 0; i < 8; i++ {
		nr := row + dx[i]
		nc := col + dy[i]
		if nr >= 1 && nc >= 1 && nr <= 8 && nc <= 8 {
			cnt++
		}
	}
	fmt.Println(cnt)
}
