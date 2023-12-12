n = int(input())
count = 0

for _ in range(n):
    x = input().split('-')    
    if int(x[1]) <= 90:
        count += 1

print(count)

