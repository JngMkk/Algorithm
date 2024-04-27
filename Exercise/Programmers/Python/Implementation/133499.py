def solution(babbling):
    can_speak = {"aya", "ye", "woo", "ma"}

    cnt = 0
    for babblin in babbling:
        for can_s in can_speak:
            if can_s * 2 not in babblin:
                babblin = babblin.replace(can_s, " ")

        if not babblin.strip():
            cnt += 1

    return cnt


babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))
