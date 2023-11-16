package main

import (
	"regexp"
	"strings"
	"unicode"
)

type Deque []interface{}

func (d *Deque) IsEmpty() bool {
	return len(*d) == 0
}

func (d *Deque) PopLeft() interface{} {
	if d.IsEmpty() {
		return nil
	}
	elem := (*d)[0]
	*d = (*d)[1:]
	return elem
}

func (d *Deque) Pop() interface{} {
	if d.IsEmpty() {
		return nil
	}
	_len := len(*d) - 1
	elem := (*d)[_len]
	*d = (*d)[:_len]
	return elem
}

func isPalindrome(s string) bool {
	s = strings.ToLower(s)
	regex := regexp.MustCompile("[^0-9a-z]")
	s = regex.ReplaceAllString(s, "")

	var deque Deque
	for _, s := range s {
		deque = append(deque, s)
	}

	for len(deque) > 1 {
		if deque.PopLeft() != deque.Pop() {
			return false
		}
	}

	return true
}

func isPalindrome2(s string) bool {
	s = strings.Map(func(r rune) rune {
		if !unicode.IsLetter(r) && !unicode.IsNumber(r) {
			return -1
		}
		return unicode.ToLower(r)
	}, s)

	left := 0
	right := len(s) - 1
	for left <= right {
		if s[left] != s[right] {
			return false
		}
		left++
		right--
	}

	return true
}
