x=list(map(int,input().split()))

a=x[2]-x[0]
b=x[0]
c=x[3]-x[1]
d=x[1]

print(min(a,b,c,d))