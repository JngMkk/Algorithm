"""
    문제

        N가지 종류의 화폐가 있음. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 함.
        이때 각 종류의 화폐는 몇 개라도 사용할 수 있음.

        예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수임.

        M원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램 작성.

        첫째 줄에 N, M이 주어짐(1 <= N <= 100, 1 <= M <= 10,000)
        이후의 N개 줄에는 각 화폐의 가치가 주어짐. 화폐의 가치는 10,000보다 작거나 같은 자연수임.

        첫째 줄에 최소 화폐 개수를 출력함.

        2 15
        2
        3

        => 5
"""

# 나의 풀이
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
d = [0] * (m + 1)

for i in range(1, m + 1):
    d[i] = d[i - 1] + 1
    for x in arr:
        if i - x < 0:
            d[i] = 0
            continue
        if d[i - x] == 0:
            continue
        elif d[i - x] > 0:
            d[i] = d[i - x] + 1

if d[m] > 0:
    print(d[m])
else:
    print(-1)


"""
    문제 해결 아이디어

        a_i = 금액 i를 만들 수 있는 최소한의 화폐 개수
        k = 각 화폐의 단위

        점화식: 각 화폐 단위인 k를 하나씩 확인하며 a_i-k를 만드는 방법이 존재하는 경우, a_i = min(a_i, a_i-k + 1), 존재하지 않는 경우, a_i = INF

    예)
        N = 3, M = 7이고, 각 화폐의 단위가 2, 3, 5인 경우

        Step 0)
            먼저 각 인덱스에 해당하는 값으로 INF(무한)의 값을 설정
            INF은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미를 가짐.
            본 문제에서는 10,001을 사용할 수 있음.

        Step 1)
            첫 번째 화폐 단위인 2를 확인 => 2원으로 만들 수 있는 화폐는 모두 갱신됨
"""

# 해답
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 초기화
d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(arr[i], m + 1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
