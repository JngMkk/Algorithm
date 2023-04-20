# https://school.programmers.co.kr/learn/courses/30/lessons/81302

from collections import deque

dx: list = [-1, 1, 0, 0]
dy: list = [0, 0, -1, 1]


def get_dist(a: int, x: int, b: int, y: int) -> int:
    return abs(a - x) + abs(b - y)


def bfs(arr: list, x: int, y: int) -> bool:
    q = deque([(x, y)])
    visited: list = [[0] * 5 for _ in range(5)]
    visited[x][y] = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if (
                na < 0
                or nb < 0
                or na > 4
                or nb > 4
                or get_dist(na, x, nb, y) > 2
                or visited[na][nb]
                or arr[na][nb] == "X"
            ):
                continue
            if arr[na][nb] == "P":
                return False
            visited[na][nb] = 1
            q.append((na, nb))
    return True


def solution(places: list) -> list:
    res = [1] * 5

    for i in range(5):
        for x in range(5):
            for y in range(5):
                if places[i][x][y] == "P":
                    if not bfs(places[i], x, y):
                        res[i] = 0
    return res


# ======================================================================================================================================
def bfs2(arr: list, x: int, y: int) -> bool:
    q: deque[tuple[int, ...]] = deque([(x, y, 0)])
    visited = set()
    visited.add((x, y))

    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                nx < 0
                or ny < 0
                or nx > 4
                or ny > 4
                or dist > 2
                or (nx, ny) in visited
                or arr[nx][ny] == "X"
            ):
                continue
            if arr[nx][ny] == "P":
                return False
            visited.add((nx, ny))
            q.append((nx, ny, dist + 1))
    return True


def solution2(places: list) -> list:
    res = [1] * 5

    for i in range(5):
        for x in range(5):
            for y in range(5):
                if places[i][x][y] == "P":
                    if not bfs2(places[i], x, y):
                        res[i] = 0
    return res
