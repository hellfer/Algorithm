n = int(input())
milk = list(map(int, input().split()))
count = 0
milk_type = 0

for i in range(n):
    if milk[i] == milk_type:
        count += 1
        milk_type = (milk_type + 1) % 3

print(count)