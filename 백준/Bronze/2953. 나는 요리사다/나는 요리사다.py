result=[]
max=0
min=0
for i in range(1,6):
    x=list(map(int,input().split()))
    result.append((i,sum(x)))
    if max<sum(x):
        max=sum(x)
        min=i
        
print(min,max)
