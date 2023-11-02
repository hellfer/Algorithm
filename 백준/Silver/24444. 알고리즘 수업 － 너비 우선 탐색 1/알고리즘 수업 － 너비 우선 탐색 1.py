from collections import deque
import sys
input=sys.stdin.readline
# 정점의 수 N, 간선의 수 M, 시작 정점 R 입력 받기
N, M, R = map(int, input().split())

# 그래프와 방문 순서 리스트 초기화
graph = [[] for _ in range(N+1)]
order = [0]*(N+1)

# 간선 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 정점을 오름차순으로 방문하기 위해 정렬
for i in range(N+1):
    graph[i].sort()

# BFS 알고리즘
def bfs(R):
    queue = deque([R])
    cnt = 1
    order[R] = cnt
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if order[i] == 0:
                queue.append(i)
                cnt += 1
                order[i] = cnt

bfs(R)

# 방문 순서 출력
for i in range(1, N+1):
    print(order[i])
