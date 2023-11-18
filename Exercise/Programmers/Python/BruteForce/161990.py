def solution(wallpaper: list[str]) -> list[int]:
    x_arr, y_arr = [], []
    len_y = len(wallpaper[0])
    for x in range(len(wallpaper)):
        for y in range(len_y):
            if wallpaper[x][y] == "#":
                x_arr.append(x)
                y_arr.append(y)

    return [min(x_arr), min(y_arr), max(x_arr) + 1, max(y_arr) + 1]


wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))  # [0, 1, 3, 4]

wallpaper = ["..........", ".....#....", "......##..", "...##.....", "....#....."]
print(solution(wallpaper))  # [1, 3, 5, 8]

wallpaper = [
    ".##...##.",
    "#..#.#..#",
    "#...#...#",
    ".#.....#.",
    "..#...#..",
    "...#.#...",
    "....#....",
]
print(solution(wallpaper))  # [0, 0, 7, 9]

wallpaper = ["..", "#."]
print(solution(wallpaper))  # [1, 0, 2, 1]
