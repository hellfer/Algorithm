while True:
    x=input().split(' ', 1)
    if x[0]=='#':
        break
    y=x[0].lower()
    z=x[1].lower()
    print(y,z.count(y))
    