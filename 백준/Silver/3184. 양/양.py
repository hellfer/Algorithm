from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
total_wolf, total_sheep = 0, 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    wolves, sheep = 0, 0
    if graph[x][y] == 'v':
        wolves += 1
    elif graph[x][y] == 'o':
        sheep += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != '#':
                queue.append((nx, ny))
                visited[nx][ny] = True
                if graph[nx][ny] == 'v':
                    wolves += 1
                elif graph[nx][ny] == 'o':
                    sheep += 1
    if wolves < sheep:
        return 0, sheep
    else:
        return wolves, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != '#' and not visited[i][j]:
            wolves, sheep = bfs(i, j)
            total_wolf += wolves
            total_sheep += sheep

print(total_sheep, total_wolf)

            