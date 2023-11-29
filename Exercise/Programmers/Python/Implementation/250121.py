def solution(data: list[list[int]], ext: str, val_ext: int, sort_by: str) -> list[list[int]]:
    index_map = {"code": 0, "date": 1, "maximum": 2, "remain": 3}

    def filter_data() -> list[list[int]]:
        idx = index_map[ext]
        return list(filter(lambda x: x[idx] < val_ext, data))

    def sort_data(data: list[list[int]]) -> list[list[int]]:
        idx = index_map[sort_by]
        return sorted(data, key=lambda x: x[idx])

    filtered_data = filter_data()
    return sort_data(filtered_data)


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"
print(solution(data, ext, val_ext, sort_by))  # [[3, 20300401, 10, 8], [1, 20300104, 100, 80]]
