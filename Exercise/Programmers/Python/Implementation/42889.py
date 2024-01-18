# https://school.programmers.co.kr/learn/courses/30/lessons/42889


def solution1(N: int, stages: "list[int]") -> "list[int]":
    cnt = [[i + 1, 0] for i in range(N)]
    for s in stages:
        if s > N:
            continue
        cnt[s - 1][1] += 1

    num = len(stages)
    for i in range(N):
        if num == 0:
            cnt[i][1] = 0
            continue
        tmp = cnt[i][1] / num
        num -= cnt[i][1]
        cnt[i][1] = tmp

    return [x[0] for x in sorted(cnt, key=lambda x: -x[1])]


def solution2(N: int, stages: "list[int]") -> "list[int]":
    from collections import Counter

    c = Counter(stages)
    challengers = len(stages)
    rate = {k: 0 for k in range(1, N + 1)}

    for stage in range(1, N + 1):
        if challengers:
            rate[stage] = c[stage] / challengers
            challengers -= c[stage]
        else:
            rate[stage] = 0

    answer = sorted(rate, key=rate.get, reverse=True)

    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution1(N, stages))  # [3, 4, 2, 1, 5]
N = 4
stages = [4, 4, 4, 4, 4]
print(solution1(N, stages))  # [4, 1, 2, 3]

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution2(N, stages))  # [3, 4, 2, 1, 5]
N = 4
stages = [4, 4, 4, 4, 4]
print(solution2(N, stages))  # [4, 1, 2, 3]
