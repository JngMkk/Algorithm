/*
문제

	N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있음. 이때 이 수열에서 x가 등장하는 횟수를 계산.
	예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력함

	단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받음.

	첫째 줄에 N가 x가 정수 형태로 공백으로 구분되어 입력 (1 <= N <= 1,000,000), (-10^9 <= x <= 10^9)

	둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됨. (-10^9 <= 각 원소의 값 <= 10^9)

	수열의 원소 중에서 값이 x인 원소의 개수를 출력함. 단, 값이 x인 원소가 하나도 없다면 -1을 출력.
*/
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func getRightIdx(a []int, target, start, end int) int {
	for start < end {
		mid := (start + end) / 2

		if a[mid] > target {
			end = mid
		} else {
			start = mid + 1
		}
	}
	return start
}

func getLeftIdx(a []int, target, start, end int) int {
	for start < end {
		mid := (start + end) / 2

		if a[mid] < target {
			start = mid + 1
		} else {
			end = mid
		}
	}
	return start
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	var arr []int
	sc.Scan()
	s := strings.Split(sc.Text(), " ")
	n, _ := strconv.Atoi(s[0])
	x, _ := strconv.Atoi(s[1])
	sc.Scan()
	s = strings.Split(sc.Text(), " ")
	for _, v := range s {
		n, _ := strconv.Atoi(v)
		arr = append(arr, n)
	}
	cnt := getRightIdx(arr, x, 0, n) - getLeftIdx(arr, x, 0, n)
	if cnt == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(cnt)
	}
}
