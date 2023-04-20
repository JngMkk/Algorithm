package main

import "fmt"

type Queue []interface{}

func (q *Queue) isEmpty() bool {
	return len(*q) == 0
}

func (q *Queue) enQueue(elem interface{}) {
	*q = append(*q, elem)
}

func (q *Queue) deQueue() interface{} {
	if q.isEmpty() {
		fmt.Println("queue is empty")
		return nil
	}
	elem := (*q)[0]
	*q = (*q)[1:]
	return elem
}

func main() {
	var q Queue

	q.enQueue(5)
	q.enQueue(2)
	q.enQueue(3)
	q.enQueue(7)
	q.deQueue()
	q.enQueue(1)
	q.enQueue(4)
	q.deQueue()
	fmt.Println(q)
}
