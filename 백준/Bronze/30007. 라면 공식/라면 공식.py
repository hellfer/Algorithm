n=int(input())

for _ in range(n):
    x,y,z=map(int,input().split())
    print(x*(z-1)+y)