import heapq


def solution(N: int, road: list[list[int]], K: int) -> int:
    def init_graph() -> list[dict[int, int]]:
        graph = {i: {} for i in range(N + 1)}
        for node1, node2, cost in road:
            if node2 in graph[node1]:
                graph[node1][node2] = min(graph[node1][node2], cost)
            else:
                graph[node1][node2] = cost

            if node1 in graph[node2]:
                graph[node2][node1] = min(graph[node2][node1], cost)
            else:
                graph[node2][node1] = cost

        return graph

    graph = init_graph()
    start_node = 1
    max_cost = 500001

    costs = [max_cost] * (N + 1)
    costs[start_node] = 0

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if costs[current_node] < current_cost:
            continue

        for neighbor, cost in graph[current_node].items():
            total_cost = current_cost + cost
            if total_cost < costs[neighbor]:
                costs[neighbor] = total_cost
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return len([cost for cost in costs if cost <= K])
