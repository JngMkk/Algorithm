def solution(x, y, n):
    """
    BFS 이용.
    x -> y로 가는 것보다 y -> x로 가면서 나누어 떨어지지 않는 수는 배제시켜 연산을 줄이는 것이 더 효율적임.

    O(N), N은 x와 y 사이의 유효한 숫자의 개수
    """
    from collections import deque

    def calculate(num, i):
        if i == 0 and num % 3 == 0:
            return num // 3
        if i == 1 and num % 2 == 0:
            return num // 2
        if i == 2:
            return num - n
        return -1

    queue = deque([(y, 0)])
    visited = set()

    while queue:
        curr_num, curr_cnt = queue.popleft()
        visited.add(curr_num)
        if curr_num == x:
            return curr_cnt

        for i in range(3):
            next_num = calculate(curr_num, i)
            if next_num >= x and next_num not in visited:
                queue.append((next_num, curr_cnt + 1))

    return -1


x = 10
y = 40
n = 5
print(solution(x, y, n))  # 2

x = 10
y = 40
n = 30
print(solution(x, y, n))  # 1

x = 2
y = 5
n = 4
print(solution(x, y, n))  # -1
