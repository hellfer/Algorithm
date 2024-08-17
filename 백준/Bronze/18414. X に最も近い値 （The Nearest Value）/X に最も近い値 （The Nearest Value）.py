# 입력 받기
X, L, R = map(int, input().split())

# 초기값 설정
closest_value = L
min_difference = abs(X - L)

# L부터 R까지 반복
for i in range(L, R + 1):
    current_difference = abs(X - i)
    if current_difference < min_difference:
        min_difference = current_difference
        closest_value = i

# 결과 출력
print(closest_value)
