m = int(input())
n = int(input())
array = [True for i in range(n + 1)]
result = []

for i in range(2, int(n ** 0.5) + 1):
    if array[i] == True:
        for j in range(i * 2, n + 1, i):
            array[j] = False

for i in range(m, n + 1):
    if i > 1 and array[i] == True:
        result.append(i)

if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
