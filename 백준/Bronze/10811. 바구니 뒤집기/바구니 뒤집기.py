n,m=map(int,input().split())

box=list(range(1,n+1))

for _ in range(m):
    x,y=map(int,input().split())
    box[x-1:y]=reversed(box[x-1:y])
    
print(' '.join(map(str,box)))