"""
    신장 트리

        그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
            - 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건은 트리의 조건이기도 함

        최소 신장 트리
            - 최소한의 비용으로 구성되는 신장 트리를 찾아야 할 때 어떻게 해야 할까?
            - 예를 들어 N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치하는 경우를 생각해보자
                - 두 도시 A, B를 선택했을 때 A에서 B로 이동하는 경로가 반드시 존재하도록 도로를 설치.
            - 간선 개수: 전체 노드 개수 - 1

    크루스칼 알고리즘

        대표적인 최소 신장 트리 알고리즘

        그리디 알고리즘으로 분류

        구체적인 동작 과정
            1. 간선 데이터를 비용에 따라 오름차순으로 정렬
            2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
                1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킴
                2) 발생하는 경우 최소 신장 트리에 포함시키지 않음
            3. 모든 간선에 대하여 2번의 과정을 반복

        크루스칼 알고리즘은 간선의 개수가 E개일 때, O(ElogE)의 시간 복잡도를 가짐

        크루스칼 알고리즘에서 가장 많은 시간을 요구하는 곳은 간선 정렬을 수행하는 부분
            - 표준 라이브러리를 이용해 E개의 데이터를 정렬하기 위한 시간 복잡도는 O(ElogE)임.
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [x for x in range(v + 1)]

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))
edges.sort()

res = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)
