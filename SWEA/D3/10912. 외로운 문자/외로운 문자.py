from collections import Counter

n = int(input())

for i in range(1, n+1):
    x = input()
    result = set()
    y = Counter(x)
    for j in x:
        if y[j] %2 != 0:
            result.add(j)
    result=sorted(result)
    if result:
        print(f'#{i} {"".join(result)}')
    else:
        print(f'#{i} Good')

