def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# 입력 처리
C = int(input())
results = []
for _ in range(C):
    n = int(input())
    divisors_count = count_divisors(n)
    results.append(f"{n} {divisors_count}")

# 결과 출력
for result in results:
    print(result)
