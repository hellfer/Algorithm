import math

n, k = map(int, input().split())
array = [True for i in range(n + 1)]
result = []
for i in range(2, n + 1):
    if array[i] == True:
        for j in range(i, n + 1, i):
            if array[j] == True:
                array[j] = False
                result.append(j)
                if len(result) == k:
                    print(result[-1])
                    break



