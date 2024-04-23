"""
힙 추가/삭제 연산은 O(log n) 시간이 소요된다.
"""


def solution(n: int, k: int, enemy: "list[int]") -> int:
    from heapq import heappop, heappush

    h: "list[int]" = []
    for round, num_enemy in enumerate(enemy, 1):
        # * 병사 수를 줄임
        n -= num_enemy
        # * 최대 힙에 현재 적의 수를 넣음
        heappush(h, -num_enemy)

        # * 만약 병사 수가 0보다 작다면
        if n < 0:
            # * 방어권이 남아 있다면
            if k:
                # * 가장 소모가 컸던 적을 꺼내서 회복시킴 (= 가장 적이 큰 라운드를 방어함)
                n += -heappop(h)
                k -= 1
            else:
                # * 방어권이 없다면 이전 라운드가 마지막 라운드임
                round -= 1
                break

    return round


def solution2(n: int, k: int, enemy: "list[int]") -> int:
    from heapq import heapify, heappushpop

    hq = enemy[:k]
    # * 방어권 만큼 최소힙에 넣음
    heapify(hq)
    for idx in range(k, len(enemy)):
        # * 가장 적은 적을 만나는 라운드를 수행함 (= 가장 적인 큰 라운드를 방어함)
        n -= heappushpop(hq, enemy[idx])
        # * n이 0보다 적다면 이전 라운드가 마지막임
        if n < 0:
            return idx

    return len(enemy)


n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(n, k, enemy))  # 5

n = 2
k = 4
enemy = [3, 3, 3, 3]
print(solution(n, k, enemy))  # 4
