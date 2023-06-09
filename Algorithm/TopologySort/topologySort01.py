"""
    위상 정렬

        사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미함.

        예시) 선수과목을 고려한 학습 순서 설정

            자료구조 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ> 알고리즘
               |                              |
               |                              |
               ㅡㅡㅡㅡㅡ> 고급 알고리즘 <ㅡㅡㅡㅡㅡㅡ

            - 위 세 과목을 모두 듣기 위한 적절한 학습 순서는?
                자료구조 -> 알고리즘 -> 고급 알고리즘 (O)
                자료구조 -> 고급 알고리즘 -> 알고리즘 (X)

    진입차수와 진출차수

        진입차수: 특정한 노드로 들어오는 간선의 개수
        진출차수: 특정한 노드에서 나가는 간선의 개수

    위상 정렬 알고리즘

        큐를 이용하는 위상 정렬 알고리즘의 동작 과정
            1. 진입차수가 0인 모든 노드를 큐에 넣음
            2. 큐가 빌 때까지 다음의 과정을 반복
                1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거함
                2) 새롭게 진입차수가 0이 된 노드를 큐에 넣음

        => 결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같음

    위상 정렬의 특징

        위상 정렬은 DAG에 대해서만 수행할 수 있음
            - DAG: 순환하지 않는 방향 그래프

        위상 정렬에서는 여러 가지 답이 존재할 수 있음
            - 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면 여러 가지 답이 존재함.

        모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있음
            - 사이클에 포함된 원소 중에서 어떠한 원소도 큐에 들어가지 못함.

        스택을 활용한 DFS를 이용해 위상 정렬을 수행할 수도 있음.

    위상 정렬 성능

        위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선을 차례대로 제거해야 함.
            - 위상 정렬 알고리즘의 시간 복잡도는 O(V+E)
"""

from collections import deque

v, e = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    res = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res.append(now)

        for node in graph[now]:
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

    for r in res:
        print(r, end=" ")


topology_sort()
