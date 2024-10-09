n, k = map(int, input().strip().split())
timings = [int(input().strip()) for _ in range(n)]

gifts = 0

for i in range(1, n):
    if timings[i-1] - timings[i] >= k:
        gifts += 1

print(gifts)