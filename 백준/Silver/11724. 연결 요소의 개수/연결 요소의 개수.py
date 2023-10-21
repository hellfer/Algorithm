from collections import deque
import sys
input=sys.stdin.readline
def bfs(v):
    queue=deque()
    queue.append(v)
    visited[v]=True
    while queue:
        x=queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

n,m=map(int,input().split())
count=0
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count+=1

print(count)
