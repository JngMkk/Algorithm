def solution(n):
    from collections import deque

    s = "124"
    arr = deque()
    while n > 0:
        n -= 1
        n, mod = divmod(n, 3)
        arr.appendleft(s[mod])
    return "".join(arr)


n = 1
print(solution(n))  # 1
n = 2
print(solution(n))  # 2
n = 3
print(solution(n))  # 4
n = 4
print(solution(n))  # 11
