from collections import deque

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    return count


m, n, k = map(int,input().split())
graph=[[0]*n for _ in range(m)]
visited=[[False]*n for _ in range(m)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(k):
    y1,x1,y2,x2=map(int,input().split())
    
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[i][j]=1

result=[]
for i in range(m):
    for j in range(n):
        if graph[i][j]==0 and not visited[i][j]:
            result.append(bfs(i,j))

print(len(result))
for i in sorted(result):
    print(i,end=' ')


