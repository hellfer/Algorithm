n=int(input())

for i in range(1,n+1):
    a,b=map(int,input().split())
    print(f'#{i} {a**2//b**2}')