def solution(data: list[list[int]], col: int, row_begin: int, row_end: int) -> int:
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    _hash = 0
    for i in range(row_begin - 1, row_end):
        _hash ^= sum(value % (i + 1) for value in data[i])

    return _hash


data = [[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]]
col = 2
row_begin = 2
row_end = 3
print(solution(data, col, row_begin, row_end))  # 4
