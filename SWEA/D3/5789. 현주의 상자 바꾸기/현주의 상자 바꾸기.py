n=int(input())

for i in range(1,n+1):
    x,y=map(int,input().split())
    result=[0] * x
    for j in range(y):
        p,q=map(int,input().split())
        for k in range(p-1,q):
            result[k]=j+1
    print(f"#{i} {' '.join(map(str, result))}")
