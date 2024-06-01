n=int(input())

for i in range(1,n+1):
    x=list(map(int,input().split()))
    y=max(x)
    print(f'Case #{i}: {y}')
