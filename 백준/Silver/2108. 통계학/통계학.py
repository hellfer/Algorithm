import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

numbers.sort()

# Arithmetic mean
mean = round(sum(numbers) / n)

# Median
median = numbers[n // 2]

# Mode
counter = Counter(numbers)
modes = counter.most_common()
if len(modes) > 1:
    if modes[0][1] == modes[1][1]:
        mode = modes[1][0]
    else:
        mode = modes[0][0]
else:
    mode = modes[0][0]

# Range
range_value = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range_value)

