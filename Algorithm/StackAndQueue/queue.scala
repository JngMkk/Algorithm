package StackAndQueue

import scala.collection.mutable

object queue {
    def main(args: Array[String]): Unit = {
        val q = mutable.Queue[Any]()
        q.enqueue(5)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(7)
        q.dequeue()
        q.enqueue(1)
        q.enqueue(4)
        q.dequeue()
        println(q)
    }
}
