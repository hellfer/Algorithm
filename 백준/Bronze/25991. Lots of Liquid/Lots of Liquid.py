def calculate_needed_container_length(n, lengths):
    total_volume = 0.0
    for length in lengths:
        total_volume += length ** 3  # Calculate the volume of each cube

    # Length of the side of the new container
    required_length = total_volume ** (1/3)
    return required_length

# 입력받기
n = int(input())
lengths = list(map(float, input().split()))

# 결과 계산
result = calculate_needed_container_length(n, lengths)

# 결과 출력
print(f"{result:.12f}")
