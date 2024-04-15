n = int(input())  # 입력 받을 숫자의 수

for j in range(1,n+1):
    x = int(input())  # 검사할 숫자 입력
    result = []  # 나누어 떨어지는 경우를 저장할 리스트
    for i in range(1, 10):  # 1부터 9까지의 숫자로 나누어 보기
        if x % i == 0:  # x가 i로 나누어 떨어지면
            z = x // i  # 나눈 몫을 구함
            if z <= 9:  # 나눈 몫이 9 이하면
                result.append((i, z))  # 결과 리스트에 추가

    # 결과 리스트에 하나라도 요소가 있으면 'Yes'를 출력, 그렇지 않으면 'No'를 출력
    if result:
        print(f'#{j} Yes')
    else:
        print(f'#{j} No')

