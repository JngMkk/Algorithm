"""
    문제

        N X M 크기의 얼음 틀이 있음.
        구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됨.
        구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주함.
        이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성.

        다음 4 X 5 얼음 틀 예시는 아이스크림이 총 3개 생성됨
        00110
        00011
        11111
        00000
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


res = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            res += 1

print(res)


"""
    문제 해결 아이디어

        이 문제는 DFS 혹은 BFS로 해결할 수 있음.
        얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다고 표현할 수 있으므로 그래프 형태로 모델링 할 수 있음.
"""
