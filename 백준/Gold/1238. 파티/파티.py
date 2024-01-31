import heapq
import sys

INF = int(1e9)

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n+1)]
reverse_graph = [[] for i in range(n+1)]

for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))
    reverse_graph[end].append((start, time))

def dijkstra(start, graph):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
    return distance

distance_to_x = dijkstra(x, reverse_graph)
distance_from_x = dijkstra(x, graph)
max_distance = max([distance_to_x[i] + distance_from_x[i] for i in range(1, n + 1)])

print(max_distance)

