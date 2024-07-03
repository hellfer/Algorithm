n, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
count = 0

left=0
right=n-1

while left < right:
    if x[left] + x[right] <= k :
        left+=1
        right-=1
        count+=1
    else:
        right-=1

print(count)

