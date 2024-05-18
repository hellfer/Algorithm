n=int(input())
for i in range(1,n+1):
    z=[]
    n,m=map(int,input().split())
    x=list(map(int,input().split()))
    y=[str(i) for i in range(1,n+1) if i not in x]
    print(f'#{i} {" ".join(y)}')
