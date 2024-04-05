def gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n

def lcm(n,m):
    return n*m//gcd(n,m)

k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    print(lcm(a,b),gcd(a,b))
