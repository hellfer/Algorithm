import sys
sys.setrecursionlimit(10**6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, arr, visited):
    visited[x][y] = True
    color = arr[x][y]
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == color:
            dfs(nx, ny, arr, visited)

n = int(input())
graph = [list(input()) for _ in range(n)]
color_blind = [[i if i == 'B' else 'R' for i in row] for row in graph]

visited1 = [[False]*n for _ in range(n)]
visited2 = [[False]*n for _ in range(n)]

res1 = res2 = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs(i, j, graph, visited1)
            res1 += 1
        if not visited2[i][j]:
            dfs(i, j, color_blind, visited2)
            res2 += 1

print(res1, res2)
