n=int(input())

for _ in range(n):
    count=0
    x,y=map(int,input().split())
    for i in range(x,y+1):
        count+=str(i).count('0')
        
    print(count)
        
        