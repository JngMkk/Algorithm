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

	var N, K int
	fmt.Fscanln(reader, &N, &K)
	cnt := 0

	for {
		target := (N / K) * K
		cnt += N - target
		N = target
		if N < K {
			break
		}
		N /= K
		cnt += 1
	}

	cnt += N - 1
	fmt.Println(cnt)
}
