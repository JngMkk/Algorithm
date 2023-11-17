def solution(park: list[str], routes: list[str]) -> list[int]:
    max_idx_lst = len(park) - 1
    max_idx_str = len(park[0]) - 1

    MOVE = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    s_lst, s_str = 0, 0
    blocked = set()
    for idx_lst, _map in enumerate(park):
        for idx_str, val in enumerate(_map):
            if val == "S":
                s_lst, s_str = idx_lst, idx_str
            elif val == "X":
                blocked.add((idx_lst, idx_str))

    for route in routes:
        direction, cnt = route.split(" ")
        move = MOVE[direction]
        d_lst, d_str = move[0], move[1]
        flag = True
        for i in range(1, int(cnt) + 1):
            n_lst = s_lst + d_lst * i
            n_str = s_str + d_str * i
            if (
                n_lst < 0
                or n_lst > max_idx_lst
                or n_str < 0
                or n_str > max_idx_str
                or (n_lst, n_str) in blocked
            ):
                flag = False
                break

        if flag:
            s_lst += d_lst * int(cnt)
            s_str += d_str * int(cnt)

    return [s_lst, s_str]


park1 = ["SOO", "OOO", "OOO"]
routes1 = ["E 2", "S 2", "W 1"]
print(solution(park1, routes1))
# [2, 1]

park2 = ["SOO", "OXX", "OOO"]
routes2 = ["E 2", "S 2", "W 1"]
print(solution(park2, routes2))
# [0, 1]

park3 = ["OSO", "OOO", "OXO", "OOO"]
routes3 = ["E 2", "S 3", "W 1"]
print(solution(park3, routes3))
# [0, 0]
