def count_digits(N):
    count = 0
    length = len(str(N))  # N의 길이(자릿수)를 계산
    for i in range(1, length):
        count += i * (10**i - 10**(i-1))  # 각 자릿수별 사용 횟수를 더함
    count += length * (N - 10**(length-1) + 1)  # 마지막 자릿수 구간의 사용 횟수를 더함
    return count

N = int(input())
result = count_digits(N)
print(result % 1234567)

