def solution(board: list[list[str]], h: int, w: int) -> int:
    n = len(board) - 1
    cnt = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh < 0 or nh > n or nw < 0 or nw > n or board[nh][nw] != board[h][w]:
            continue
        cnt += 1

    return cnt


board = [
    ["blue", "red", "orange", "red"],
    ["red", "red", "blue", "orange"],
    ["blue", "orange", "red", "red"],
    ["orange", "orange", "red", "blue"],
]
h = 1
w = 1
print(solution(board, h, w))  # 2

board = [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
h = 0
w = 1
print(solution(board, h, w))  # 1
