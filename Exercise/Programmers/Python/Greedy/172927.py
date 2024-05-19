def solution(picks, minerals):
    minerals = minerals[: sum(picks) * 5]
    fatigue = []
    dia, iron, stone = [0] * 3
    stone_map = {"d": 25, "i": 5, "s": 1}
    div, mod = divmod(len(minerals), 5)
    div += 1 if mod else 0
    for i, mineral in enumerate(minerals):
        dia += 1
        iron += 5 if mineral[0] == "d" else 1
        stone += stone_map[mineral[0]]
        if (i + 1) % 5 == 0:
            fatigue.append((stone, iron, dia))
            dia, iron, stone = [0] * 3

    if mod:
        fatigue.append((stone, iron, dia))

    fatigue.sort(reverse=True)
    answer = 0
    cursor = 0
    for i, pick in enumerate(picks):
        for _ in range(pick):
            if cursor >= div:
                break
            answer += fatigue[cursor][2 - i]
            cursor += 1

    return answer


picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals))  # 12

picks = [0, 1, 1]
minerals = [
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "iron",
    "iron",
    "iron",
    "iron",
    "iron",
    "diamond",
]
print(solution(picks, minerals))  # 50

picks = [0, 0, 1]
minerals = ["stone", "stone", "stone", "stone", "stone", "diamond"]
print(solution(picks, minerals))  # 5
