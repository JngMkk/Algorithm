def solution(scoville: list[int], K: int) -> int:
    from heapq import heapify, heappop, heappush

    cnt = 0
    heapify(scoville)
    while True:
        least = heappop(scoville)
        if least >= K:
            break
        _next = heappop(scoville)
        heappush(scoville, least + _next * 2)
        cnt += 1

    return cnt


"""
list의 길이를 N이라고 했을 때,

heapify(list): 리스트를 힙으로 변환 => 시간 복잡도 O(N)
heappop(list): 최소 힙에서 최소 요소를 제거하고 반환 => O(log N)
heappush(list, value): 요소를 힙에 추가 => O(log N)

while loop에서 heappop은 두 번, heappush는 한 번 호출됨.
loop 반복의 총 시간 복잡도: O(3log N) => O(log N)
loop는 최악의 경우 (N - 1)번 반복될 수 있음. (모든 요소를 한 번씩 처리했을 때)
따라서, loop의 전체 시간 복잡도: O(Nlog N)

전체 시간 복잡도: heapify(list)의 O(N)과 while loop의 O(Nlog N)을 합한 것 => O(Nlog N)
입력 리스트의 크기에 따라 로그 선형적으로 증가하는 복잡도를 가짐
"""


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
