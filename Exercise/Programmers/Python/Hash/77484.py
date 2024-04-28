def solution(lottos, win_nums):
    win_map = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    erased = lottos.count(0)
    matched_cnt = len(set(lottos) & set(win_nums))

    return [win_map[matched_cnt + erased], win_map[matched_cnt]]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))  # [3, 5]

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))  # [1, 6]

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))  # [1, 1]
