# 해적 수 입력
N = int(input())

# 결과를 저장할 리스트
result = []

# 해적 번호 출력 및 "Go!" 추가
for i in range(1, N + 1):
    result.append(str(i))  # 해적 번호를 문자열로 추가
    if i % 6 == 0:  # 6의 배수일 경우 "Go!" 추가
        result.append("Go!")

# 마지막 해적 후 "Go!" 추가
if N % 6 != 0:
    result.append("Go!")

# 결과 출력
print(" ".join(result))
