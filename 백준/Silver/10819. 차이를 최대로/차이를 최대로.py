from itertools import permutations

n=int(input())

x=list(map(int,input().split()))

max_sum=0

for i in permutations(x):
    count=0
    for j in range(n-1):
        count+=abs(i[j]-i[j+1])
    max_sum=max(max_sum,count)
    
print(max_sum)