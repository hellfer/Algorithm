# 입력 받기
A, B = map(int, input().split())

# M 계산
M = (B - A) / 400

# 확률 P 계산
P = 1 / (1 + 10**M)

# 결과 출력
print(P)
