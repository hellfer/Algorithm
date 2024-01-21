import math
n=int(input())

for _ in range(n):
    x,y=map(int,input().split())
    result=math.factorial(y)//(math.factorial(x)*math.factorial(y-x))
    print(result)