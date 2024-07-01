n = int(input())
m = int(input())
x = list(map(int, input().split()))
x.sort()

count = 0
left = 0
right = n - 1

while left < right:
    current_sum = x[left] + x[right]
    if current_sum == m:
        count += 1
        left += 1
        right -= 1
    elif current_sum < m:
        left += 1
    else:
        right -= 1

print(count)
