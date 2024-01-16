def solution(topping: "list[int]") -> int:
    from collections import Counter

    answer = 0

    a = set()
    len_b = len(set((topping)))
    div = len_b // 2
    counter = Counter(topping)
    while topping:
        top = topping.pop()
        a.add(top)

        counter[top] -= 1
        if counter[top] == 0:
            len_b -= 1

        if len(a) >= div and len(a) == len_b:
            answer += 1

    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))  # 2

topping = [1, 2, 3, 1, 4]
print(solution(topping))  # 0
