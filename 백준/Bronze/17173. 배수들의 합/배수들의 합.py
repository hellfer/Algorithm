n,m=map(int,input().split())
graph=list(map(int,input().split()))
result=0
for i in range(1,n+1):
    for j in graph:
        if i%j==0:
            result+=i
            break
            
print(result)