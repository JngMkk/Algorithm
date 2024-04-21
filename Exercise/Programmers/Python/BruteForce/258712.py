def solution(friends: "list[str]", gifts: "list[str]") -> int:
    from collections import defaultdict

    gift_idx_map: "dict[str, int]" = defaultdict(int)
    gift_map: "dict[str, dict[str, int]]" = defaultdict(lambda: defaultdict(int))
    gift_cnt: "dict[str, int]" = defaultdict(int)
    for gift in gifts:
        sender, receiver = gift.split()
        gift_map[sender][receiver] += 1
        gift_idx_map[sender] += 1
        gift_idx_map[receiver] -= 1

    for friend in friends:
        for f in friends:
            gift_cnt_diff = gift_map[friend][f] - gift_map[f][friend]
            if gift_cnt_diff > 0:
                gift_cnt[friend] += 1
            elif gift_cnt_diff == 0:
                gift_idx_diff = gift_idx_map[friend] - gift_idx_map[f]
                if gift_idx_diff > 0:
                    gift_cnt[friend] += 1

    if not gift_cnt:
        return 0
    return max(gift_cnt.values())


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = [
    "muzi frodo",
    "muzi frodo",
    "ryan muzi",
    "ryan muzi",
    "ryan muzi",
    "frodo muzi",
    "frodo ryan",
    "neo muzi",
]
print(solution(friends, gifts))  # 2

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = [
    "alessandro brad",
    "alessandro joy",
    "alessandro conan",
    "david alessandro",
    "alessandro david",
]
print(solution(friends, gifts))  # 4

friends = ["a", "b", "c"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]
print(solution(friends, gifts))  # 0
