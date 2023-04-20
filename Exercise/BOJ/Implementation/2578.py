# https://www.acmicpc.net/problem/2578

"""
입력
첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 빙고판에 쓰여진 수와 사회자가 부르는 수는 각각 1부터 25까지의 수가 한 번씩 사용된다.

출력
첫째 줄에 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력한다.

예제 입력 1
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
예제 출력 1
15
"""

import sys


def check_right_diag(array: list) -> bool:
    for i in range(5):
        flag = False
        for j in range(5):
            if i == j and array[i][j]:
                flag = True
        if not flag:
            return False
    return True


def check_left_diag(array: list) -> bool:
    for i in range(4, -1, -1):
        flag = False
        for j in range(5):
            if 4 - i == j and array[i][j]:
                flag = True
        if not flag:
            return False
    return True


def check_horizon(array: list, r_ind: int) -> bool:
    for tf in array[r_ind]:
        if not tf:
            return False
    return True


def check_vertical(array: list, c_ind: int) -> bool:
    for i in range(5):
        if not array[i][c_ind]:
            return False
    return True


inp = sys.stdin.readline
tf_board = [[False] * 5 for _ in range(5)]
index_board = dict()
announcement = []

for i in range(5):
    board = list(map(int, inp().split()))
    for j in range(5):
        index_board[board[j]] = (i, j)

for _ in range(5):
    announcement.extend(list(map(int, inp().split())))

cnt = 0
for i in range(25):
    row, col = index_board[announcement[i]]
    tf_board[row][col] = True

    if i < 4:
        continue

    if row == col:
        if check_right_diag(tf_board):
            cnt += 1
    if 4 - row == col:
        if check_left_diag(tf_board):
            cnt += 1

    if check_horizon(tf_board, row):
        cnt += 1
    if check_vertical(tf_board, col):
        cnt += 1

    if cnt >= 3:
        print(i + 1)
        break
