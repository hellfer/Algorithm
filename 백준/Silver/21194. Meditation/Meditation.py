n,m=map(int,input().split())
result=[]
for _ in range(n):
    x=int(input())
    result.append(x)
    
result.sort()

print(sum(result[n-m:n]))
