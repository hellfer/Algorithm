def factorial_last_non_zero_digit(n):
    y = 1
    for i in range(1, n + 1):
        y *= i
        while y % 10 == 0:
            y //= 10
        y %= 100000  # 큰 수를 처리하기 위해 적당히 자릅니다.
    return y % 10

import sys
input = sys.stdin.read

data = input().split()
for num in data:
    n = int(num)
    result = factorial_last_non_zero_digit(n)
    print(f'{n:5} -> {result}')
