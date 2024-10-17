# 학교의 수 입력
N = int(input())

# 남는 사과의 총 개수를 저장할 변수
total_leftover = 0

# 각 학교에 대한 입력 처리
for _ in range(N):
    students, apples = map(int, input().split())
    # 남는 사과 계산
    leftover = apples % students
    total_leftover += leftover

# 결과 출력
print(total_leftover)
