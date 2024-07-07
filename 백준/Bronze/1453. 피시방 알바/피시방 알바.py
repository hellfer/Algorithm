from collections import Counter

n = int(input())
x = list(map(int, input().split()))
y = Counter(x)
sum=0

for i in y:
    sum+=(y[i]-1)
    
print(sum)
