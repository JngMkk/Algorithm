def solution(cards1: list[str], cards2: list[str], goal: list[str]) -> str:
    idx1, idx2 = 0, 0

    for word in goal:
        if len(cards1) > idx1 and word == cards1[idx1]:
            idx1 += 1

        elif len(cards2) > idx2 and word == cards2[idx2]:
            idx2 += 1

        else:
            return "No"

    return "Yes"


def solution2(cards1: list[str], cards2: list[str], goal: list[str]) -> str:
    cards1[:] = cards1[::-1]
    cards2[:] = cards2[::-1]

    for g in goal:
        if cards1 and g == cards1[-1]:
            cards1.pop()

        elif cards2 and g == cards2[-1]:
            cards2.pop()

        else:
            return "No"

    return "Yes"


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))  # "Yes"

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))  # "No"
