t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    for _ in range(m):
        print('X' * n)
    print()