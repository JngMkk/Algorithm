def solution(board):
    from collections import deque

    def bfs(start_r, start_c):
        cost = [[[MAX for _ in range(N)] for _ in range(N)] for _ in range(4)]
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque([(start_r, start_c, None, 0)])
        for i in range(4):
            cost[i][start_r][start_c] = 0

        while queue:
            curr_r, curr_c, curr_direc, curr_cost = queue.popleft()
            for direction in range(4):
                dr, dc = move[direction]
                nr, nc = curr_r + dr, curr_c + dc
                if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 1:
                    continue

                n_cost = curr_cost + 100
                if curr_direc is not None and direction != curr_direc:
                    n_cost += 500

                if cost[direction][nr][nc] > n_cost:
                    cost[direction][nr][nc] = n_cost
                    queue.append((nr, nc, direction, n_cost))

        return cost

    N = len(board)
    MAX = float("inf")
    cost = bfs(0, 0)
    answer = MAX
    for i in range(4):
        answer = min(answer, cost[i][N - 1][N - 1])
    return answer
