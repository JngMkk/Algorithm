"""
    최단 경로 문제

        최단 경로 알고리즘은 가장 짧은 경로를 찾는 알고리즘을 의미

        다양한 문제 상황
            - 한 지점에서 다른 한 지점까지의 최단 경로
            - 한 지점에서 다른 모든 지점까지의 최단 경로
            - 모든 지점에서 다른 모든 지점까지의 최단 경로

        각 지점은 그래프에서 노드로 표현

        지점 간 연결된 도로는 그래프에서 간선으로 표현


    다익스트라 최단 경로 알고리즘 개요

        특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로를 계산

        다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작함
            - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않음.

        다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류됨.
            - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복.

        동작 과정
            1. 출발 노드를 설정
            2. 최단 거리 테이블을 초기화.
            3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택함.
            4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신함.
            5. 위 과정에서 3번과 4번을 반복.

        특징
            - 그리디 알고리즘: 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
            - 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않음.
                - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해할 수 있음.
            - 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됨.
                - 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 함.
"""


"""
    다익스트라 간단 구현 방법

        단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)함.

        성능
            - 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 함
            - 따라서 전체 시간 복잡도는 O(V^2)임.
            - 일반적으로 코딩 테스트의 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 이 코드로 문제를 해결할 수 있음.
                - 하지만 노도의 개수가 10,000개 이상이라면 !!? ㅠㅠ
"""
import sys

inp = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, inp().split())
start = int(inp())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만듦
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, inp().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    ind = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            ind = i
    return ind


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for tup in graph[start]:
        distance[tup[0]] = tup[1]

    # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for _ in range(n - 1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True

        # 현재 노드와 연결된 다른 노드를 확인
        for tup in graph[now]:
            cost = distance[now] + tup[1]
            if cost < distance[tup[0]]:
                distance[tup[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
