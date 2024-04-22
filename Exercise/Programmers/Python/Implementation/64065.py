def solution(s: str) -> "list[int]":
    from collections import Counter

    counter: "Counter[int]" = Counter()
    num = ""
    for _str in s:
        if _str.isdigit():
            num += _str
        else:
            if num:
                counter[int(num)] += 1
                num = ""

    return list(map(lambda x: x[0], counter.most_common()))


def solution2(s: str) -> "list[int]":
    import re
    from collections import Counter

    # findall(pattern: str | Pattern[str], string: str, flags: _FlagsType = 0) -> list[Any]
    # string에서 pattern과 일치하는 부분을 모두 찾아 list로 return
    print(re.findall("\d+", s))
    counter: "Counter[str]" = Counter(re.findall("\d+", s))
    return list(map(lambda x: int(x[0]), counter.most_common()))


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))  # [2, 1, 3, 4]
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))  # [2, 1, 3, 4]
s = "{{20,111},{111}}"
print(solution(s))  # [111, 20]
s = "{{123}}"
print(solution(s))  # [123]
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))  # [3, 2, 4, 1]
