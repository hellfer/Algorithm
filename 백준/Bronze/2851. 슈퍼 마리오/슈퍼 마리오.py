result = []
count = 0
x = 0
diff = 100

for _ in range(10):
    n = int(input())
    result.append(n)

for i in range(10):
    count += result[i]
    if abs(100 - count) <= diff:
        x = count
        diff = abs(100 - count)
    if count > 100:
        break

print(x)

