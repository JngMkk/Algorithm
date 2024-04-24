def solution(k: int, d: int) -> int:
    cnt = 0

    biggest = d**2
    for x in range(0, d + 1, k):
        # 주어진 x 값에 대해 원점으로부터 거리 'd' 이내에 있을 수 있는 y좌표의 최대값
        y = (biggest - x**2) ** (1 / 2)
        cnt += y // k + 1

    return int(cnt)


k = 2
d = 4
print(solution(k, d))  # 6

k = 1
d = 5
print(solution(k, d))  # 26
