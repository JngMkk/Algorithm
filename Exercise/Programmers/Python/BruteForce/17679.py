def solution(m, n, board):
    board = [list(string) for string in board]
    move = [[1, 0], [0, 1], [1, 1]]
    answer = 0
    while True:
        can_erase_blocks = set()
        for r in range(m - 1):
            for c in range(n - 1):
                if board[r][c] == "-":
                    continue
                blocks = [(r, c)]
                flag = True
                for dr, dc in move:
                    nr = r + dr
                    nc = c + dc
                    if board[nr][nc] != board[r][c]:
                        flag = False
                        break
                    blocks.append((nr, nc))

                if flag:
                    for block in blocks:
                        can_erase_blocks.add(block)

        if not can_erase_blocks:
            break
        answer += len(can_erase_blocks)
        for row, col in can_erase_blocks:
            board[row][col] = "-"

        for c in range(n):
            for r in range(m):
                for x in range(1, m - r):
                    if board[x][c] == "-":
                        board[x - 1][c], board[x][c] = board[x][c], board[x - 1][c]

    return answer


def solution2(m, n, board):
    board = [list(b) for b in zip(*board)]
    move = [[1, 0], [0, 1], [1, 1]]
    cnt = 0
    while True:
        can_erase = set()
        for r in range(n - 1):
            for c in range(m - 1):
                if board[r][c] == "-":
                    continue
                flag = True
                blocks = [(r, c)]
                for dr, dc in move:
                    nr = r + dr
                    nc = c + dc
                    if board[nr][nc] != board[r][c]:
                        flag = False
                        break
                    blocks.append((nr, nc))

                if flag:
                    for block in blocks:
                        can_erase.add(block)

        if not can_erase:
            break

        cnt += len(can_erase)
        for row, col in can_erase:
            board[row][col] = "-"
        for row, elems in enumerate(board):
            board[row] = ["-"] * elems.count("-") + [elem for elem in elems if elem != "-"]

    return cnt


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))  # 14

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))  # 15

m = 5
n = 6
board = ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]
print(solution(m, n, board))  # 24
