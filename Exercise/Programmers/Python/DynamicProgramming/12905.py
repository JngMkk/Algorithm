def solution(board: "list[list[int]]") -> int:
    rows = len(board)
    cols = len(board[0])

    area_board = [[0] * (cols + 1) for _ in range(rows + 1)]
    _max = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if board[r - 1][c - 1] != 0:
                area_board[r][c] = (
                    min(area_board[r - 1][c], area_board[r][c - 1], area_board[r - 1][c - 1]) + 1
                )
                _max = max(_max, area_board[r][c])

    return _max**2


board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(board))  # 9
board = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board))  # 4
board = [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print(solution(board))  # 1
