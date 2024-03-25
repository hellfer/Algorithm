n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    z = pow(x, y, 10)
    if z == 0:
        print(10)
    else:
        print(z)
