"""
    문제

        어떤 나라에는 N개의 도시가 있음.
        각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있음.

        하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 함.
        예를 들어 X에서 Y로 향하는 통로는 있지만 Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없음.
        또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요됨.

        어느 날 C라는 도시에서 위급상황이 발생함. 그래서 최대한 많은 도시로 메시지를 보내고자 함.
        메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것임.

        각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때,
        도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인가?

        첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어짐.
        1 <= N <= 30,000    1 <= M <= 200,000    1 <= C <= N

        둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어짐.
        이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미
        (1 <= X, Y <= N     1 <= Z <= 1,000)

        첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력

입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
"""
import heapq

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
INF = int(1e9)
dist = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

hq = []
heapq.heappush(hq, (0, c))
dist[c] = 0

while hq:
    dis, now = heapq.heappop(hq)
    if dist[now] < dis:
        continue

    for tup in graph[now]:
        cost = dis + tup[1]
        if cost < dist[tup[0]]:
            dist[tup[0]] = cost
            heapq.heappush(hq, (cost, tup[0]))

cnt, time = 0, 0
for d in dist:
    if d != INF:
        cnt += 1
        time = max(time, d)

print(cnt - 1, time)


"""
    문제 해결 아이디어

        핵심 아이디어: 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있음.

        N과 M의 범위가 충분히 크기 때문에 우선순위 큐를 활용한 다익스트라 알고리즘을 구현함.
"""
