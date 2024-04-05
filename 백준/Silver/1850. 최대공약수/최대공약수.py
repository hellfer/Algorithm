import math

def gcd(n,m):
    while m!=0:
        n,m=m,n%m
    return n

a,b=map(int,input().split())

x='1' * gcd(a,b)

print(x)