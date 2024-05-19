def solution(stones, k):
    """슬라이딩 윈도우 O(N)"""

    from collections import deque

    queue = deque()
    min_max = 200000001
    for i in range(len(stones)):
        if queue and queue[0] < i - k + 1:
            queue.popleft()  # 윈도우 범위를 벗어난 인덱스는 제거
        while queue and stones[queue[-1]] <= stones[i]:
            queue.pop()  # 현재 돌이 queue에 있는 돌보다 크거나 같으면, queue에서 돌을 제거
        queue.append(i)

        if i >= k - 1:
            min_max = min(min_max, stones[queue[0]])  # 윈도우 형성 후 queue의 최댓값과 비교
    return min_max


def solution2(stones, k):
    """
    주어진 mid 값으로 징검다리를 건널 수 있는가?로 문제를 변환하여 이분 탐색 가능.
    주어진 mid 값(가정된 최대 사람 수)에 대해 징검다리를 건널 수 있거나 없거나 두 가지 결과만 존재.
    """

    answer = 0
    left, right = 1, max(stones)

    while left <= right:
        mid = (left + right) // 2
        count = 0
        for stone in stones:
            if stone < mid:
                count += 1
                if count >= k:
                    break
            else:
                count = 0

        if count >= k:  # mid명이 건널 수 없음.
            right = mid - 1
        else:  # mid명이 건널 수 있음
            answer = mid
            left = mid + 1

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution2(stones, k))  # 3
