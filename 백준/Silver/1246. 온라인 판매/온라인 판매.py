n,m=map(int,input().split())

x=[int(input()) for _ in range(m)]

x.sort(reverse=True)

count=0
result=0

for i,j in enumerate(x):
    y=min(i+1,n)
    z=y*j
    if z>count:
        count=z
        result=j
        
print(result,count)
