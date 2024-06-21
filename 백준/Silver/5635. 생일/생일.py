from datetime import datetime

# 학생 수 입력
n = int(input())

students = []

# 학생 정보 입력 및 리스트에 저장
for _ in range(n):
    data = input().split()
    name = data[0]
    day = int(data[1])
    month = int(data[2])
    year = int(data[3])
    # 날짜 객체로 저장
    birthdate = datetime(year, month, day)
    students.append((name, birthdate))

# 나이가 적은 순서로 정렬 (최근 생일일수록 나이가 적음)
students.sort(key=lambda x: x[1], reverse=True)

# 가장 나이가 적은 사람
youngest = students[0][0]
# 가장 나이가 많은 사람
oldest = students[-1][0]

# 결과 출력
print(youngest)
print(oldest)
