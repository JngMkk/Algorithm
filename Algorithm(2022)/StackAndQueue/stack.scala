package StackAndQueue

import scala.collection.mutable

object stack {
    def main(args: Array[String]): Unit = {
        val s = mutable.Stack[Any]()
        s.push(5)
        s.push(2)
        s.push(3)
        s.push(7)
        s.pop()
        s.push(1)
        s.push(4)
        s.pop()
        println(s)  // Stack(1, 3, 2, 5)
    }
}
