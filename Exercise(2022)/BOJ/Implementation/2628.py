# https://www.acmicpc.net/problem/2628

import sys

inp = sys.stdin.readline
a, b = map(int, inp().split())

row = [0, b]
col = [0, a]
n = int(inp())
for _ in range(n):
    x, y = map(int, inp().split())
    if x == 0:
        row.append(y)
    else:
        col.append(y)

row.sort()
col.sort()

max_r = 0
for i in range(len(row) - 1):
    max_r = max(max_r, row[i + 1] - row[i])

max_c = 0
for i in range(len(col) - 1):
    max_c = max(max_c, col[i + 1] - col[i])

print(max_r * max_c)
