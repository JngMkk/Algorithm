from heapq import heappush, heappop
from functools import wraps


class DoublePriorityQueue:
    def __init__(self) -> None:
        self.max_heap = []
        self.min_heap = []
        self.counter = 0
        self.counter_map = {}

    def gc(_heap: str):
        def wrapper(func):
            @wraps(func)
            def __gc(self, *args, **kwargs):
                heap = getattr(self, _heap)
                while heap and heap[0][1] not in self.counter_map:
                    heappop(heap)
                return func(self, *args, **kwargs)

            return __gc

        return wrapper

    def add(self, x):
        self.counter_map[self.counter] = x
        heappush(self.min_heap, (x, self.counter))
        heappush(self.max_heap, (-x, self.counter))
        self.counter += 1

    @gc("min_heap")
    def pop_min(self):
        if not self.min_heap:
            return None

        v, c = heappop(self.min_heap)
        del self.counter_map[c]
        return v

    @gc("max_heap")
    def pop_max(self):
        if not self.max_heap:
            return None

        v, c = heappop(self.max_heap)
        del self.counter_map[c]
        return -v

    @gc("min_heap")
    def get_min(self):
        if not self.min_heap:
            return None
        return self.min_heap[0][0]

    @gc("max_heap")
    def get_max(self):
        if not self.max_heap:
            return None
        return -self.max_heap[0][0]


def solution(operations):
    queue = DoublePriorityQueue()
    for operation in operations:
        oper, num = operation.split()
        num = int(num)
        if oper == "I":
            queue.add(num)
            continue

        if not queue.counter_map:
            continue

        if num < 1:
            queue.pop_min()
        else:
            queue.pop_max()

    if not queue.counter_map:
        return [0, 0]
    return [queue.get_max(), queue.get_min()]


operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))  # [0, 0]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))  # [333, -45]
