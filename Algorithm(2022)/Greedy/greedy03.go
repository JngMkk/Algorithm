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

	var input string
	fmt.Fscanln(reader, &input)
	s := []rune(input)
	res := s[0] - '0'

	for i := 1; i < len(s); i++ {
		n := s[i] - '0'
		if n < 2 || res < 2 {
			res += n
		} else {
			res *= n
		}
	}

	fmt.Println(res)
}
