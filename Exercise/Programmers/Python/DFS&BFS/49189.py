def solution(n, edges):
    from collections import deque

    def bfs():
        visited = [0] * (n + 1)

        queue = deque([(1, 0)])
        visited[1] = 1
        while queue:
            node, cost = queue.popleft()
            for x in graph[node]:
                if not visited[x]:
                    visited[x] = 1
                    costs[cost + 1] += 1
                    queue.append((x, cost + 1))

        return cost

    graph = [[] for _ in range(n + 1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    costs = [0] * n
    return costs[bfs()]


n = 6
edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edges))  # 3
