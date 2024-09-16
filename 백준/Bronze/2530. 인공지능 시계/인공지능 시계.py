# 입력 받기
A, B, C = map(int, input().split())
D = int(input())

# 현재 시각을 초로 변환
current_seconds = A * 3600 + B * 60 + C

# 요리 시간을 추가
total_seconds = current_seconds + D

# 시, 분, 초로 변환
hours = (total_seconds // 3600) % 24
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# 결과 출력
print(hours, minutes, seconds)
