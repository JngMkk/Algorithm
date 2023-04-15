"""
    문제

        N명의 병사가 무작위로 나열되어 있음. 각 병사는 특정한 값의 전투력을 보유하고 있음.

        병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 함.
        다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 함.

        또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용함.
        그러면서도 남아 있는 병사의 수가 최대가 되도록 하고 싶음.

        예를 들어, N = 7일 때 나열된 병사들의 전투력이 다음과 같다고 가정

        병사 번호:  1   2   3   4   5   6   7
        전투 역량:  15  11  4   8   4   2   4

        이때 3번 병사와 6번 병사를 열외시키면, 다음과 같이 남아 있는 병사의 수가 내림차순의 형태가 되며 5명이 됨.
        이는 남아 있는 병사의 수가 최대가 되도록 하는 방법.

        1   2   4   5   7
        15  11  8   5   4

        병사에 대한 정보가 주어졌을 때, 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력하는 프로그램 작성.

        첫째 줄에 N이 주어짐. (1 <= N <= 2000)
        둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어짐. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수(1 <= P <= 10,000,000)

7
15 11 4 8 5 2 4

=> 2
"""

n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

"""
    문제 해결 아이디어

        이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같음.

        예를 들어 하나의 수열 array = {4, 2, 5, 8, 4, 11, 15}이 있다고 하면
        이 수열의 가장 긴 증가하는 부분 수열은 {4, 5, 8, 11, 15}임.

        본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환할 수 있으므로, LIS 알고리즘을 조금 수정하여 적용함으로써 정답을 도출할 수 있음.

        가장 긴 증가하는 부분 수열 (LIS) 알고리즘을 확인해 보자.

        D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

        점화식
            - 모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
"""
