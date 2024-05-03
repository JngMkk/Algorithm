def solution(rows, columns, queries):
    _map = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    answer = []

    for query in queries:
        r_start, r_end, c_start, c_end = query[0] - 1, query[2] - 1, query[1] - 1, query[3] - 1
        r_cursor, c_cursor = r_start, c_start
        arr = []
        while c_cursor < c_end:
            arr.append((_map[r_cursor][c_cursor], (r_cursor, c_cursor + 1)))
            c_cursor += 1
        while r_cursor < r_end:
            arr.append((_map[r_cursor][c_cursor], (r_cursor + 1, c_cursor)))
            r_cursor += 1
        while c_cursor > c_start:
            arr.append((_map[r_cursor][c_cursor], (r_cursor, c_cursor - 1)))
            c_cursor -= 1
        while r_cursor > r_start:
            arr.append((_map[r_cursor][c_cursor], (r_cursor - 1, c_cursor)))
            r_cursor -= 1

        if arr:
            answer.append(min(map(lambda x: x[0], arr)))
            for elem, idx in arr:
                _map[idx[0]][idx[1]] = elem
        else:
            answer.append(_map[r_start][c_cursor])

    return answer


def solution2(rows, columns, queries):
    board = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    answer = []

    for r1, c1, r2, c2 in queries:
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        stack = []

        for i in range(c1, c2 + 1):
            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]

        for i in range(r1 + 1, r2 + 1):
            stack.append(board[i][c2])
            board[i][c2] = stack[-2]

        for i in range(c2 - 1, c1 - 1, -1):
            stack.append(board[r2][i])
            board[r2][i] = stack[-2]

        for i in range(r2 - 1, r1 - 1, -1):
            stack.append(board[i][c1])
            board[i][c1] = stack[-2]

        answer.append(min(stack))
    return answer


rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(rows, columns, queries))  # [8, 10, 25]

rows = 3
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(rows, columns, queries))  # [1, 1, 5, 3]

rows = 100
columns = 97
queries = [[1, 1, 100, 97]]
print(solution(rows, columns, queries))  # [1]
