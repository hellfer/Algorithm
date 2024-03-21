from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))  # (x, y) 좌표와 이동 횟수를 함께 큐에 저장
    visited[x][y] = True
    while queue:
        a, b, count = queue.popleft()
        if a == x2 and b == y2:
            return count  # 목표 지점에 도달했을 때 이동 횟수 반환
        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))  # 이동 횟수를 1 증가시켜 큐에 추가
                visited[nx][ny] = True
    return -1  # 목표 지점에 도달할 수 없는 경우 -1 반환

result = bfs(x1, y1)
print(result)
