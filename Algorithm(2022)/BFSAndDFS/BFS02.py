"""
    문제

        사용자는 N X M 크기의 직사각형 형태의 미로에 갇힘. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 함.

        사용자의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있음.
        이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있음. 미로는 반드시 탈출할 수 있는 형태로 제시됨.

        이때 사용자가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산함.

        입력 예시
        5 6
        101010
        111111
        000001
        111111
        111111
"""
from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            # 처음 방문 시에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))


"""
    문제 해결 아이디어

        BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색함.

        상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일함
            - 따라서 (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있음.

"""
