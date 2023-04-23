"""
    문제

        여행가 A는 N X N 크기의 정사각형 공간 위에 서 있음. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있음.
        가장 왼쪽 위 자표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당함.
        여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)임.
        우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있음.

        계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있음.
            - L: 왼쪽으로 한 칸 이동
            - R: 오른쪽으로 한 칸 이동
            - U: 위로 한 칸 이동
            - D: 아래로 한 칸 이동

        이때 여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시됨.
        예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됨.

        N = 5인 계획서 : R - R - R - U - D - D (공간 밖은 무시)
"""

# 나의 풀이(해답과 같았음)
n = int(input())
plan = list(input().split())

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
direction = ["L", "R", "D", "U"]

x, y = 1, 1

for p in plan:
    for i in range(len(direction)):
        if p == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)


"""
    문제 해결 아이디어

        일련의 명령에 따라서 개체를 차례대로 이동시킨다는 점에서 시뮬레이션 유형으로도 분류되며 구현이 중요한 대표적인 문제 유형.
"""