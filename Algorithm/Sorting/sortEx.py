"""
    문제

        사용자는 두 개의 배열 A와 B를 가지고 있음.
        두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수.

        사용자는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데,
        바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말함.

        사용자의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것임.

        N, K, 그리고 배열 A와 B의 정보가 주어졌을 때,
        최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성.

        예를 들어 N = 5, K = 3이고
        배열 A = [1, 2, 5, 4, 3]
        배열 B = [5, 5, 6, 6, 5]

        5 3
        1 2 5 4 3
        5 5 6 6 5

        출력 예시 : 26
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))


"""
    문제 해결 아이디어

        핵심 아이디어 : 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체함.

        가장 먼저 배열 A, B가 주어지면 A에 대해 오름차순 정렬하고, B에 대해 내림차순 정렬함.

        이후에 두 배열의 원소를 첫 번째 인덱스부터 차례로 확인하면서 A의 원소가 B의 원소보다 작을 때에만 교체를 수행함.

        이 문제에서는 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로,
        최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 함.
"""