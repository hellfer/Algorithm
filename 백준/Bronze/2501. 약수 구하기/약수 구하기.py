# 입력을 받습니다.
N, K = map(int, input().split())

# N의 약수들을 저장할 리스트
divisors = []

# 1부터 N까지의 수를 돌면서 약수를 찾습니다.
for i in range(1, N + 1):
    if N % i == 0:
        divisors.append(i)

# 약수의 개수가 K보다 적다면 0을 출력합니다.
if len(divisors) < K:
    print(0)
else:
    # K번째 약수를 출력합니다.
    print(divisors[K - 1])
