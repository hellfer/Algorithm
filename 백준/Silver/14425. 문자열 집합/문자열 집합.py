import sys
input=sys.stdin.readline
n,m = map(int,input().split())
a=[]
count=0
for i in range(n):
    x=input().strip()
    a.append(x)
for j in range(m):
    y=input().strip()
    if y in a:
        count+=1
print(count)



