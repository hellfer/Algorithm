t=int(input())

for _ in range(t):
    x=int(input())
    y=list(map(int,input().split()))
    print(min(y), max(y))