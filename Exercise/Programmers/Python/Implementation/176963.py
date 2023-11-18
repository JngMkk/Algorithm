def solution(name: list[str], yearning: list[int], photo: list[list[str]]) -> list[int]:
    name_yearn_mapp = {n: y for n, y in zip(name, yearning)}

    answer = []
    for pho in photo:
        score = 0
        for p in pho:
            if p in name_yearn_mapp:
                score += name_yearn_mapp[p]
        answer.append(score)

    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [
    ["may", "kein", "kain", "radi"],
    ["may", "kein", "brin", "deny"],
    ["kon", "kain", "may", "coni"],
]
print(solution(name, yearning, photo))  # [19, 15, 6]

name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
print(solution(name, yearning, photo))  # [67, 0, 55]

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may"], ["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name, yearning, photo))  # [5, 15, 0]
