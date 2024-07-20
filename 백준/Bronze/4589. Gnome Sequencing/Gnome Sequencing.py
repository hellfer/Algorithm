t = int(input())
print('Gnomes:')
for _ in range(t):
    x,y,z=map(int,input().split())
    if x<=y and y<=z:
        print('Ordered')
    elif z<=y and y<=x:
        print('Ordered')
    else:
        print('Unordered')