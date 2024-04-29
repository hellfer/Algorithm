n, m = map(int, input().split())
x = 1  # 현재 숫자
y = 0  # 현재 숫자가 나타난 횟수
result = 0  # 결과값을 저장할 변수

for i in range(1, m+1):
    if i >= n:
        result += x
    y += 1
    if y == x:  # 현재 숫자 x가 x번 반복됐는지 확인
        x += 1  # 다음 숫자로 넘어감
        y = 0  # 카운터 초기화
        
print(result)  # 최종 합계 출력