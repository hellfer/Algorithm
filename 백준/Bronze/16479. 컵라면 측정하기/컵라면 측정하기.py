def calculate_height_squared(K, D1, D2):
    term = (D1 - D2) / 2
    height_squared = K**2 - term**2
    return height_squared

# 입력 받기
K = int(input())
D1, D2 = map(int, input().split())

# 높이의 제곱 계산
height_squared = calculate_height_squared(K, D1, D2)

# 결과 출력
print(f"{height_squared:.6f}")
