package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var cnt int = 0
	var coin [4]int = [4]int{500, 100, 50, 10}
	var N int
	fmt.Fscanln(reader, &N)

	for _, c := range coin {
		cnt += N / c
		N %= c
	}

	fmt.Println(cnt)
}
