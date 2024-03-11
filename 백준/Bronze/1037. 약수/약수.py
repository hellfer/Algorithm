# 약수의 개수 입력받기
n = int(input())

# 약수들을 입력받아 리스트에 저장
divisors = list(map(int, input().split()))

# 최소값과 최대값 찾기
min_divisor = min(divisors)
max_divisor = max(divisors)

# 최소값과 최대값을 곱하여 원래의 수 구하기
original_number = min_divisor * max_divisor

# 결과 출력
print(original_number)
