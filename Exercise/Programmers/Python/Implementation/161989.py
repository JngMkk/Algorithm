def solution(n: int, m: int, section: list[int]) -> int:
    cnt = 1
    x = section.pop() + 1 - m
    while section:
        _x = section.pop()
        if _x < x:
            x = _x + 1 - m
            cnt += 1

    return cnt


n, m = 8, 4
section = [2, 3, 6]
print(solution(n, m, section))  # 2

n, m = 5, 4
section = [1, 3]
print(solution(n, m, section))  # 1

n, m = 4, 1
section = [1, 2, 3, 4]
print(solution(n, m, section))  # 4
