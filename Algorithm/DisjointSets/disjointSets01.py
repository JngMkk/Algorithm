"""
    서로소 집합 자료구조

        서로소 집합: 공통 원소가 없는 두 집합을 의미

        서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조

        서로소 집합 자료구조는 두 종류의 연산을 지원함
            - 합집합(Union): 두 개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산
            - 찾기(Find): 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산

        서로소 집합 자료구조는 합치기, 찾기 자료구조라고 불리기도 함(Union Find)

        여러 개의 합치기 연산이 주어졌을 때 서로소 집합 자료구조의 동작 과정
            1. 합집합(Union) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인
                1) A와 B의 루트 노드 A', B'를 각각 찾음
                2) A'를 B'의 부모 노드로 설정
            2. 모든 합집합 연산을 처리할 때까지 1번의 과정을 반복

        기본적인 구현 방법 문제점
            - 합집합 연산이 편햐오디게 이루어지는 경우 찾기(Find) 함수가 비효율적으로 동작
            - 최악의 경우에는 찾기(Find) 함수가 모든 노드를 다 확인하게 되어 시간 복잡도가 O(V)

        해결 => 경로 압축
            - 찾기(Find) 함수를 최적화하기 위한 방법으로 경로 압축을 이용할 수 있음
                - 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신함.
"""


# 기본 구현. 특정 원소가 속한 집합을 찾기(루트)
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 경로 압축(시간 복잡도 개선)
def find_parent_path_compression(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")
print()

print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")
print()
