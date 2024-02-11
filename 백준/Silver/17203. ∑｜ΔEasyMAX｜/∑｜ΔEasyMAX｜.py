n,m=map(int,input().split())
a=list(map(int,input().split()))
result=[0]*(n-1)
for i in range(n-1):
    result[i]=abs(a[i]-a[i+1])
    
for _ in range(m):
    x,y=map(int,input().split())
    b=sum(result[x-1:y-1])
    print(b)
        