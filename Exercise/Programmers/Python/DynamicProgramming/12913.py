def solution(land: "list[list[int]]") -> int:
    def find_prev_max(arr: "list[int]", curr_idx: int) -> int:
        return max(arr[:curr_idx] + arr[curr_idx + 1 :])

    N = len(land)
    for i in range(1, N):
        for j in range(4):
            land[i][j] = land[i][j] + find_prev_max(land[i - 1], j)

    return max(land[-1])


land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
print(solution(land))  # 16
