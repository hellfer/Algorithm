# 입력 받기
A, B = map(int, input().split())

# 가능한 최대 치즈 개수
max_cheese = min(B, A - 1)

# 최대 치즈버거 크기 계산
max_size = 2 * max_cheese + 1

# 결과 출력
print(max_size)
