def solution(n, s):
    div, mod = divmod(s, n)
    if div == 0:
        return [-1]

    answer = [div] * n
    if mod == 0:
        return answer

    idx = n - 1
    while mod > 0:
        answer[idx] = answer[idx] + 1
        idx -= 1
        mod -= 1

    return answer


n = 2
s = 9
print(solution(n, s))  # [4, 5]

n = 2
s = 1
print(solution(n, s))  # [-1]

n = 2
s = 8
print(solution(n, s))  # [4, 4]

n = 3
s = 10
print(solution(n, s))
