def solution(weights: list[int]) -> int:
    from collections import Counter

    cnt = 0
    counter = Counter(weights)
    for k, v in counter.items():
        cnt += v * (v - 1) // 2
        cnt += v * counter[k * 2]
        cnt += v * counter[k * 3 / 2]
        cnt += v * counter[k * 4 / 3]

    return cnt


weights = [100, 180, 360, 100, 270, 100, 100]
print(solution(weights))  # 4
