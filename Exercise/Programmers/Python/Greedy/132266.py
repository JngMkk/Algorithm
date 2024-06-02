def solution(n, roads, sources, destination):
    from collections import deque

    graph = [[] for _ in range(n + 1)]
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    dist = [-1] * (n + 1)
    dist[destination] = 0
    queue = deque([(destination, 0)])
    while queue:
        node, cost = queue.popleft()
        for x in graph[node]:
            if dist[x] == -1:
                dist[x] = cost + 1
                queue.append((x, cost + 1))

    return [dist[source] for source in sources]


n = 3
roads = [[1, 2], [2, 3]]
sources = [2, 3]
destination = 1
print(solution(n, roads, sources, destination))  # [1, 2]

n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5
print(solution(n, roads, sources, destination))  # [2, -1, 0]
