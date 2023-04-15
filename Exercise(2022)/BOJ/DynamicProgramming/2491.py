# https://www.acmicpc.net/problem/2491

"""
문제
0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나(같은 것 포함), 혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라.

예를 들어 수열 1, 2, 2, 4, 4, 5, 7, 7, 2 의 경우에는 1 ≤ 2 ≤ 2 ≤ 4 ≤ 4 ≤ 5 ≤ 7 ≤ 7 이 가장 긴 구간이 되므로 그 길이 8을 출력한다. 수열 4, 1, 3, 3, 2, 2, 9, 2, 3 의 경우에는 3 ≥ 3 ≥ 2 ≥ 2 가 가장 긴 구간이 되므로 그 길이 4를 출력한다. 또 1, 5, 3, 6, 4, 7, 1, 3, 2, 9, 5 의 경우에는 연속해서 커지거나 작아지는 수열의 길이가 3 이상인 경우가 없으므로 2를 출력하여야 한다.

입력
첫째 줄에는 수열의 길이 N이 주어지고, 둘째 줄에는 N개의 숫자가 빈칸을 사이에 두고 주어진다. N은 1 이상 100,000 이하의 정수이다.

출력
첫째 줄에 가장 긴 길이를 출력한다.

예제 입력 1
9
1 2 2 4 4 5 7 7 2
예제 출력 1
8
예제 입력 2
9
4 1 3 3 2 2 9 2 3
예제 출력 2
4
예제 입력 3
11
1 5 3 6 4 7 1 3 2 9 5
예제 출력 3
2
"""

n = int(input())
arr = list(map(int, input().split()))

dp1, dp2 = [1] * n, [1] * n

for i in range(1, n):
    if arr[i] <= arr[i - 1]:
        dp1[i] = max(dp1[i], dp1[i - 1] + 1)
    if arr[i] >= arr[i - 1]:
        dp2[i] = max(dp2[i], dp2[i - 1] + 1)

print(max(max(dp1), max(dp2)))

# ===========================================

n = int(input())
arr = list(map(int, input().split()))

cnt1, cnt2 = 1, 1
max_cnt1, max_cnt2 = 1, 1

for i in range(1, n):
    cnt1 += 1
    cnt2 += 1
    if arr[i] > arr[i - 1]:
        if max_cnt2 < cnt2:
            max_cnt2 = cnt2 - 1
        cnt2 = 1
    elif arr[i] < arr[i - 1]:
        if max_cnt1 < cnt1:
            max_cnt1 = cnt1 - 1
        cnt1 = 1

print(max(cnt1, cnt2, max_cnt1, max_cnt2))
