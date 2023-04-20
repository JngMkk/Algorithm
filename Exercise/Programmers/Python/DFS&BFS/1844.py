# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps: list[list[int]]) -> int:
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    q: deque[tuple[int, ...]] = deque()
    q.append((0, 0, 1))

    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx <= n - 1 and ny >= 0 and ny <= m - 1:
                if maps[nx][ny] == 1 or maps[nx][ny] > c + 1:
                    maps[nx][ny] = c + 1
                    if nx == n - 1 and ny == m - 1:
                        return c + 1
                    q.append((nx, ny, c + 1))

    return -1
