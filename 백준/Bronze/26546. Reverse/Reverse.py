t=int(input())

for _ in range(t):
    x,y,z=input().split()
    result=""
    result+=x
    y=int(y)
    z=int(z)
    k=x[:y]+x[z:]
    print(k)