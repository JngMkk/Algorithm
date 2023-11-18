def solution(s: str, skip: str, index: int) -> str:
    def get_moved_char(origin_char: str) -> str:
        uni = ord(origin_char)
        move = 0
        while move < index:
            uni += 1
            if uni > _max:
                uni = _min

            if uni in skips:
                continue

            move += 1

        return chr(uni)

    answer = ""
    skips = {ord(x) for x in skip}
    _min, _max = ord("a"), ord("z")
    for char in s:
        answer += get_moved_char(char)

    return answer


def solution2(s: str, skip: str, index: int) -> str:
    answer = ""
    can_have_alpha_set = {chr(x) for x in range(ord("a"), ord("z") + 1)} - set(skip)
    can_have_alpha_list = sorted(can_have_alpha_set)
    can_have_alpha_dict = {alpha: idx for idx, alpha in enumerate(can_have_alpha_list)}
    l = len(can_have_alpha_list)
    for char in s:
        answer += can_have_alpha_list[(can_have_alpha_dict[char] + index) % l]

    return answer


s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))  # happy
print(solution2(s, skip, index))
