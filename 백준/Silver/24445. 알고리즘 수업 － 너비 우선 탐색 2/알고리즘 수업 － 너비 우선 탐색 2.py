from collections import deque
import sys
input=sys.stdin.readline
n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n+1):
    graph[i].sort(reverse=True)
def bfs(v):
    queue=deque([v])
    count=1
    visited[v]=1
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==0:
                queue.append(i)
                count+=1
                visited[i]=count
bfs(v)
for i in range(1,n+1):
    print(visited[i])