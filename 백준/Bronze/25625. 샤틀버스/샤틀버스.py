# 입력 받기
x, y = map(int, input().split())

# 민준이가 버스에 탑승할 수 있는 최소 시간
min_wait_time = (y + x) % (2 * x)

# 결과 출력
print(min_wait_time)

