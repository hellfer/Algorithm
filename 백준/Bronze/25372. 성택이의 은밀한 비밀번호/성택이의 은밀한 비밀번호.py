n=int(input())
for _ in range(n):
    x=input()
    if len(x)>=6 and len(x)<=9:
        print('yes')
    else:
        print('no')