def solution(queue1, queue2):
    answer = -1
    s1, s2 = sum(queue1), sum(queue2)

    # 1. 같아질 가능성이 있는가?
    if (s1 + s2) % 2 == 0:
        from collections import deque

        # 2. 그리디
        n = len(queue1)
        queue1, queue2 = deque(queue1), deque(queue2)
        while True:
            answer += 1
            if answer == n * 4:
                answer = -1
                break
            if s1 > s2:
                elem = queue1.popleft()
                queue2.append(elem)
                s1 -= elem
                s2 += elem
            elif s1 < s2:
                elem = queue2.popleft()
                queue1.append(elem)
                s1 += elem
                s2 -= elem
            else:
                break

    return answer


queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
print(solution(queue1, queue2))  # 2

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))  # 7

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))  # -1
