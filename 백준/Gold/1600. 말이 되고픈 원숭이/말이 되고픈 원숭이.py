from collections import deque
dx1 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy1 = [1, 2, 2, 1, -1, -2, -2, -1]
dx2 = [-1, 0, 1, 0]
dy2 = [0, 1, 0, -1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0)) # x, y, k
    visited[0][0][0] = True

    while queue:
        x, y, k = queue.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][k] - 1

        if k < K: # 말처럼 움직일 수 있는 경우
            for i in range(8):
                nx= x + dx1[i]
                ny= y + dy1[i]
                if 0 <= nx < H and 0 <= ny < W and not grid[nx][ny] and not visited[nx][ny][k+1]:
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k+1))

        # 평범하게 움직이는 경우
        for i in range(4):
            nx, ny = x + dx2[i], y + dy2[i]
            if 0 <= nx < H and 0 <= ny < W and not grid[nx][ny] and not visited[nx][ny][k]:
                visited[nx][ny][k] = visited[x][y][k] + 1
                queue.append((nx, ny, k))

    return -1

K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

print(bfs())

