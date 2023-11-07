import sys
input=sys.stdin.readline
count=[0]*10001
n=int(input())
for _ in range(n):
    x=int(input())
    count[x]+=1
for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)

