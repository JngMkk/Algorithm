def solution(n, works):
    from heapq import heappush, heappop, heapify

    if sum(works) <= n:
        return 0

    works = [-work for work in works]
    heapify(works)
    for _ in range(n):
        work = -heappop(works)
        if not work:
            break
        heappush(works, -(work - 1))

    return sum(map(lambda x: x**2, works))


works = [4, 3, 3]
n = 4
print(solution(n, works))  # 12
works = [2, 1, 2]
n = 1
print(solution(n, works))  # 6
works = [1, 1]
n = 3
print(solution(n, works))  # 0
