import sys
import heapq
input=sys.stdin.readline

INF=float('inf')

n,m,start=map(int,input().split())
graph=[[] for _ in range(n+1)]
result=[[] for _ in range(n+1)]

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
    result[y].append((x,z))
    
def dijkstra(start,graph):
    distance=[INF]*(n+1)
    queue=[]
    distance[start]=0
    heapq.heappush(queue,(0,start))
    while queue:
        a,b=heapq.heappop(queue)
        if distance[b]<a:
            continue
        for i in graph[b]:
            cost=a+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(queue,(cost,i[0]))
    return distance

q=dijkstra(start,result)
w=dijkstra(start,graph)
max_distance=max([q[i]+w[i] for i in range(1,n+1)])

print(max_distance)