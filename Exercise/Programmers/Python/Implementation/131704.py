def solution(order: "list[int]") -> int:
    stack: list[int] = []
    cnt = 0
    for i in range(1, len(order) + 1):
        if i == order[cnt]:
            cnt += 1
            while stack and stack[-1] == order[cnt]:
                stack.pop()
                cnt += 1
        else:
            stack.append(i)

    return cnt


order = [4, 3, 1, 2, 5]
print(solution(order))  # 2
order = [5, 4, 3, 2, 1]
print(solution(order))  # 5
