n, m = map(int, input().split())

x=list(map(int,input().split()))
y=list(map(int,input().split()))

z=x+y

z.sort()

print(' '.join(map(str,z)))
