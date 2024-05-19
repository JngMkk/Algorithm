def solution(maps):
    from collections import deque

    def find_elem_indices():
        indices = {}
        for i in range(r):
            for j in range(c):
                if maps[i][j] in "SLE":
                    indices[maps[i][j]] = (i, j)
                if len(indices) == 3:
                    return indices["S"], indices["L"], indices["E"]
        return indices["S"], indices["L"], indices["E"]

    def bfs(start, lever, exit):
        queue = deque([(start[0], start[1], 0)])
        distance = [[[0, 0] for _ in range(c)] for _ in range(r)]

        while queue:
            curr_r, curr_c, is_reached_lever = queue.popleft()
            curr_distance = distance[curr_r][curr_c][is_reached_lever]
            for i in range(4):
                nr = curr_r + dr[i]
                nc = curr_c + dc[i]
                if (
                    nr < 0
                    or nr >= r
                    or nc < 0
                    or nc >= c
                    or maps[nr][nc] == "X"
                    or distance[nr][nc][is_reached_lever]
                ):
                    continue

                n_distance = curr_distance + 1
                if (nr, nc) == lever:
                    queue.clear()
                    distance[nr][nc][1] = n_distance
                    queue.append((nr, nc, 1))
                    break

                if is_reached_lever and (nr, nc) == exit:
                    return n_distance

                distance[nr][nc][is_reached_lever] = n_distance
                queue.append((nr, nc, is_reached_lever))

        return -1

    r = len(maps)
    c = len(maps[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start, lever, _exit = find_elem_indices()
    return bfs(start, lever, _exit)


maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
print(solution(maps))  # 16

maps = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]
print(solution(maps))  # -1
