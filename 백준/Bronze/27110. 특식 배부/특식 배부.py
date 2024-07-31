t=int(input())
y=0
x=list(map(int,input().split()))

for i in x:
    if i<=t:
        y+=i
    else:
        y+=t
        
print(y)