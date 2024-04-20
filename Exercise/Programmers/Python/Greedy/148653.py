def solution(storey: int) -> int:
    cnt = 0
    while storey > 0:
        storey, moves = divmod(storey, 10)
        if moves > 5 or (moves == 5 and storey % 10 >= 5):
            moves = 10 - moves
            storey += 1
        cnt += moves

    return cnt


storey = 16
print(solution(storey))  # 6
storey = 2554
print(solution(storey))  # 16
