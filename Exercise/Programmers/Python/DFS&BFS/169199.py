def solution(board):
    from collections import deque

    def find_start():
        for i in range(len_r):
            for j in range(len_c):
                if board[i][j] == "R":
                    return i, j
        return -1, -1

    def bfs():
        queue = deque([(r, c, 0)])
        while queue:
            curr_r, curr_c, cnt = queue.popleft()
            for i in range(4):
                nr, nc = curr_r, curr_c
                dr, dc = move[i][0], move[i][1]
                n_cnt = cnt
                while (
                    (0 <= nr + dr < len_r)
                    and (0 <= nc + dc < len_c)
                    and board[nr + dr][nc + dc] != "D"
                ):
                    nr += dr
                    nc += dc

                n_cnt += 1
                if board[nr][nc] == "G":
                    return n_cnt

                if count_map[nr][nc] <= n_cnt:
                    continue

                count_map[nr][nc] = n_cnt
                queue.append((nr, nc, n_cnt))

        return -1

    len_r = len(board)
    len_c = len(board[0])
    r, c = find_start()
    if r < 0:
        return -1

    count_map = [[float("inf")] * len_c for _ in range(len_r)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return bfs()


board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))  # 7

board = [".D.R", "....", ".G..", "...D"]
print(solution(board))  # -1
