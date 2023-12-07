import sys
input=sys.stdin.readline

n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]
a=0
b=0
c=0

def check(x,y,n):
    global a,b,c
    paper=graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper != graph[i][j]:
                for k in range(3):
                    for l in range(3):
                        check(x+k*n//3,y+l*n//3,n//3)
                return
    if paper == -1:
        a+=1
    elif paper == 0:
        b+=1
    else:
        c+=1

check(0,0,n)
print(a)
print(b)
print(c)

        
            
            