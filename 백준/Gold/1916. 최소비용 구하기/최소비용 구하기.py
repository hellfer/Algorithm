import sys
import heapq
input=sys.stdin.readline

n=int(input())
m=int(input())
INF=float('inf')
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
    
start,end=map(int,input().split())
def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance[start]=0
    while queue:
        a,b=heapq.heappop(queue)
        if distance[b]<a:
            continue
        for i in graph[b]:
            cost=a+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(queue,(cost,i[0]))
                
dijkstra(start)
print(distance[end])