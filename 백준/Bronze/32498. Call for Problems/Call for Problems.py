n = int(input())

excluded_count = 0

for _ in range(n):
    d = int(input())
    if d % 2 != 0:
        excluded_count += 1

print(excluded_count)
