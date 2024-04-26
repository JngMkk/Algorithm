def solution(n, t, m, p):
    def convert(num):
        """10진법을 주어진 진법으로 변환"""

        div, mod = divmod(num, n)
        if div == 0:
            return nums[mod]
        return convert(div) + nums[mod]

    nums = "0123456789ABCDEF"
    strs = []
    for i in range(t * m):
        strs.append(convert(i))

    strings = "".join(strs)  # 게임에서 나온 모든 숫자
    answer = []
    for i in range(t):
        order = m * i + (p - 1)
        answer.append(strings[order])

    return "".join(answer)


n = 2
t = 4
m = 2
p = 1
print(solution(n, t, m, p))  # "0111"

n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))  # "02468ACE11111111"

n = 16
t = 16
m = 2
p = 2
print(solution(n, t, m, p))  # "13579BDF01234567"
