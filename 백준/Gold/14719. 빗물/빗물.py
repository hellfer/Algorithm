n,m=map(int,input().split())
x=list(map(int,input().split()))

a=[0]*(m)
a[0]=x[0]
for i in range(1,m):
    a[i]=max(a[i-1], x[i])
    
b=[0]*(m)
b[-1]=x[-1]
for i in range(m-2,-1,-1):
    b[i]=max(b[i+1],x[i])
    
result=0
for i in range(m):
    result+=min(a[i],b[i])-x[i]
    
print(result)