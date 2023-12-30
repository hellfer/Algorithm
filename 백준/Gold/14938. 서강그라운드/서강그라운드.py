import sys
input = sys.stdin.readline
INF = int(1e9)

# 지역의 수(n), 수색 범위(m), 경로의 수(r)을 입력받습니다.
n, m, r = map(int, input().split())

# 각 지역에서 얻을 수 있는 아이템의 수를 입력받습니다.
items = [0] + list(map(int, input().split()))

# 2차원 리스트(그래프)를 만들고, 모든 값을 무한으로 초기화합니다.
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화합니다.
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화합니다.
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 점화식에 따라 플로이드 워셜 알고리즘을 수행합니다.
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 각 지역에서 수색 범위 내에 있는 지역의 아이템을 모두 합한 값을 구하고, 그 중 최대값을 찾습니다.
result = 0
for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            temp += items[j]
    result = max(result, temp)

# 결과를 출력합니다.
print(result)
