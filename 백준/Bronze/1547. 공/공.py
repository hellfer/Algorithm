n=int(input())

box=[1]+[0]*2

for _ in range(n):
    x,y=map(int,input().split())
    box[x-1],box[y-1]=box[y-1],box[x-1]
    
for i in range(3):
    if box[i]==1:
        print(i+1)
