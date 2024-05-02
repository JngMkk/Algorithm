def solution(sequence, k):
    n = len(sequence)
    answer = [0, 0]
    min_interval = n
    start, end, _sum = [0] * 3

    for end, item in enumerate(sequence):
        _sum += item
        while _sum > k:
            _sum -= sequence[start]
            start += 1

        if _sum == k and (interval := end - start) < min_interval:
            answer = [start, end]
            min_interval = interval

    return answer


sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))  # [2, 3]

sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence, k))  # [6, 6]

sequence = [2, 2, 2, 2, 2]
k = 6
print(solution(sequence, k))  # [0, 2]
