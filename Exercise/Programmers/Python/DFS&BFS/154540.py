def solution(maps: list[str]) -> list[int]:
    from collections import deque

    def bfs(row: int, col: int) -> int:
        queue = deque([(row, col)])
        days = int(maps[row][col])
        maps[row][col] = "X"

        while queue:
            r, c = queue.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < len_r and 0 <= nc < len_c and maps[nr][nc].isdigit():
                    days += int(maps[nr][nc])
                    queue.append((nr, nc))
                    maps[nr][nc] = "X"

        return days

    len_r = len(maps)
    len_c = len(maps[0])
    dr = [-1, 1, 0, 0]  # 행 이동
    dc = [0, 0, -1, 1]  # 열 이동
    maps = [list(row) for row in maps]

    islands = []
    for r in range(len_r):
        for c in range(len_c):
            if maps[r][c].isdigit():
                days = bfs(r, c)
                islands.append(days)

    if not islands:
        return [-1]
    return sorted(islands)


"""
행의 길이를 r, 열의 길이를 c라고 했을 때,

1. list comprehension: O(r*c)
2. 이중 loop 구문: O(r*c)
    - BFS while loop
        : 각 섬을 찾을 때마다 수행됨. BFS의 시간 복잡도는 탐색해야 할 노드의 수에 선형적으로 비례함.
        : 최악의 경우, BFS는 전체 맵을 탐색해야 할 수도 있으므로 O(r*c)의 시간 복잡도를 가질 수 있음.
        : 그러나, 각 섬에 대해 BFS 수행이 겹치지 않으므로, 즉, 한 번 BFS를 수행하여 섬을 탐색하면, 그 섬의 모든 부분은 다시 탐색되지 않음.
        : 따라서, 최악의 경우 전체 맵을 한 번만 탐색.
        : 전체 시간 복잡도가 이중 loop와 중첩되는 것처럼 보이지만 실제로는 O(r*c)
3. return 정렬 부분
    : 정렬 과정은 섬의 개수에 따라 달라짐.
    : 최악의 경우 모든 칸이 섬의 일부일 수 있음. 따라서, 이 부분의 시간 복잡도는 O((r*c) * log(r*c))이 될 수 있음.

전체 시간 복잡도: O((r*c) * log (r*c))
                n=r=c일 경우, O(n^2 * logn)
"""


maps = ["X591X", "X1X5X", "X231X", "1XXX1"]
print(solution(maps))  # [1, 1, 27]

maps = ["XXX", "XXX", "XXX"]
print(solution(maps))  # -1
