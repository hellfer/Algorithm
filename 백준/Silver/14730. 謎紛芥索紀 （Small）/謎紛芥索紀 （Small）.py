t=int(input())
count=0
for _ in range(t):
    x,y=map(int,input().split())
    count+=x*y
    
print(count)