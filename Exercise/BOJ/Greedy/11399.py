"""
https://www.acmicpc.net/problem/11399

O(N log N)
"""

N = int(input())
people = sorted(map(int, input().split()))

_sum = 0
for i in range(N):
    _sum += people.pop() * (i + 1)

print(_sum)

"""
5
1 3 3 4 2
"""
