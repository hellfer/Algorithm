n=int(input())

for _ in range(n):
    x=int(input())
    if abs(x)%2==0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')