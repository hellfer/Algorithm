from collections import deque

def bfs():
    queue=deque()
    queue.append(n)
    visited[n]=0
    while queue:
        x=queue.popleft()
        for nx in [x-1,x+1,x*2]:
            if 0<=nx<100001 and visited[nx]==-1:
                if nx == x*2:
                    visited[nx]=visited[x]
                    queue.appendleft(nx)
                else:
                    visited[nx]=visited[x]+1
                    queue.append(nx)
visited=[-1]*100001
n,m=map(int,input().split())
bfs()
print(visited[m])
