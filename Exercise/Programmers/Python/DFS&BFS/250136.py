def solution(land: list[list[int]]) -> int:
    from collections import deque

    def bfs(row: int, col: int) -> tuple[int, int, int]:
        """return chunk's size, minimum column index, maximum column index"""

        queue = deque([(row, col)])  # 노드 큐 삽입
        land[row][col] = 0  # 방문 처리
        size = 1  # 해당 덩어리 사이즈
        _min, _max = col, col  # 해당 덩어리 가장 작은 컬럼 인덱스, 가장 큰 컬럼 인덱스
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + d_row[i]
                nc = c + d_col[i]
                if 0 <= nr < len_row and 0 <= nc < len_col and land[nr][nc]:
                    queue.append((nr, nc))  # 노드 큐 삽입
                    land[nr][nc] = 0  # 방문 처리
                    size += 1
                    _min, _max = min(_min, nc), max(_max, nc)

        return size, _min, _max

    len_row = len(land)
    len_col = len(land[0])
    d_row = [-1, 1, 0, 0]
    d_col = [0, 0, -1, 1]
    size_with_col_idx = [0] * len_col  # 해당 idx에 뚫었을 때 덩어리 size

    for row in range(len_row):
        for col in range(len_col):
            if land[row][col]:
                size, min_col_idx, max_col_idx = bfs(row, col)
                for i in range(min_col_idx, max_col_idx + 1):
                    size_with_col_idx[i] += size

    if not size_with_col_idx:  # 덩어리 없을 시 0 반환
        return 0

    return max(size_with_col_idx)


"""
이중 루프: O(R * C)
    - BFS 함수: 맵의 크기에 선형적으로 비례함. 각 영역은 한 번만 탐색됨. O(R * C)
    - column idx 배열 update: column 길이의 C(최악의 경우)의 반복을 수반하므로, O(C)

최댓값 찾기: O(C)

전체 시간 복잡도: O(N * M^2)
"""


land = [
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1],
]
print(solution(land))  # 9

land = [
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
]
print(solution(land))  # 16
