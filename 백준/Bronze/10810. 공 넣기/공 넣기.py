n,m=map(int,input().split())

graph=[0]*n

for _ in range(m):
    x,y,z=map(int,input().split())
    for i in range(x-1,y):
        graph[i]=z
        
print(' '.join(map(str,graph)))