from collections import Counter


def solution(keymap: list[str], targets: list[str]) -> list[int]:
    dic: dict[str, int] = {}
    for key in keymap:
        for i, k in enumerate(key, 1):
            if k in dic:
                if i < dic[k]:
                    dic[k] = i
            else:
                dic[k] = i

    answer = []
    for target in targets:
        cnt = 0
        for t in target:
            if t in dic:
                cnt += dic[t]
            else:
                cnt = -1
                break

        answer.append(cnt)

    return answer


def solution2(keymap: list[str], targets: list[str]) -> list[int]:
    dic: dict[str, int] = {}
    for key in keymap:
        for i, k in enumerate(key, 1):
            if k in dic:
                if i < dic[k]:
                    dic[k] = i
            else:
                dic[k] = i

    answer = []
    for target in targets:
        counter = Counter(target)
        cnt = 0
        for key, count in counter.items():
            if key in dic:
                cnt += count * dic[key]
            else:
                cnt = -1
                break

        answer.append(cnt)

    return answer


keymap = ["ABACD", "BCEFD"]
targets = ["ABCD", "AABB"]
print(solution(keymap, targets))  # [9, 4]

keymap = ["AGZ", "BSSS"]
targets = ["ASA", "BGZ"]
print(solution(keymap, targets))  # [4, 6]

keymap = ["AA"]
targets = ["B"]
print(solution(keymap, targets))  # [-1]

keymap = ["AA"]
targets = ["XA"]
print(solution(keymap, targets))
