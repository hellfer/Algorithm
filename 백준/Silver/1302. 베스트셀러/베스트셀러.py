from collections import Counter

n = int(input())
result = []

for _ in range(n):
    x = input()
    result.append(x)

counter = Counter(result)
most_common = counter.most_common()
max_count = most_common[0][1]
result2 = []

for x, count in most_common:
    if count == max_count:
        result2.append(x)

print(sorted(result2)[0])

    
