"""
    다익스트라 알고리즘 개선된 구현 방법

        단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 힙 자료구조를 이용

        다익스트라 알고리즘이 동작하는 기본 원리는 동일
            - 현재 가장 가까운 노드를 저장해 놓기 위해 힙 자료구조를 추가적으로 이용한다는 점이 다름
            - 현재의 최단 거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용

        성능
            - 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 O(ElogV)임.
            - 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 처리되지 않음.
                - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수만큼 연산이 수행될 수 있음.
            - 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사함.
                - 시간 복잡도를 O(ElogE)로 판단할 수 있음
                - 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있음
                    - O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV)

    우선순위 큐

        우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조.

        Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원함.

    힙(Heap)

        우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나

        최소 힙과 최대 힙이 있음.

    우선순위 큐 구현 방식

        리스트
            - 삽입 시간: O(1)
            - 삭제 시간: O(N)

        힙
            - 삽입 시간: O(logN)
            - 삭제 시간: O(logN)
"""
import heapq


# 오름차순 힙 정렬
def ascendingHeapsort(iterable):
    h = []
    result = []

    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))

    return result


# 내림차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


# result = ascendingHeapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# print(result)

# result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
# print(result)


# 개선된 다익스트라 알고리즘
import sys

inp = sys.stdin.readline
INF = int(1e9)

n, m = map(int, inp().split())
start = int(inp())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, inp().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for tup in graph[now]:
            cost = dist + tup[1]
            if cost < distance[tup[0]]:
                distance[tup[0]] = cost
                heapq.heappush(q, (cost, tup[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
