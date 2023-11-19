# 문제 점수와 번호를 저장하는 리스트 생성
result = []

# 8번 반복하면서 점수 입력받기
for i in range(8):
    score = int(input())
    result.append((score, i + 1))

# 점수 순으로 정렬하기
result.sort()

# 가장 높은 5개의 점수 선택하기
top_five = result[3:]

# 가장 높은 5개의 점수 합산하기
total_score = sum(score for score, _ in top_five)

# 합산 점수 출력하기
print(total_score)

# 가장 높은 5개의 점수가 어떤 문제에서 나왔는지 출력하기
problem_numbers = sorted(number for _, number in top_five)
for number in problem_numbers:
    print(number)


