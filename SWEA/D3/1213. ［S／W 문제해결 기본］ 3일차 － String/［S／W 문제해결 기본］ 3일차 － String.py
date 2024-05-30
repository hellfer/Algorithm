for i in range(1, 11):
    n = int(input())  # 테스트 케이스 번호 입력 (사용되지 않음)
    x = input()  # 찾을 문자열 입력
    y = input()  # 검색할 문장 입력
    count = 0
    
    # 검색할 문장을 순회하며 찾을 문자열의 출현 횟수 계산
    for j in range(len(y)):
        if y[j:j + len(x)] == x:
            count += 1
            
    print(f'#{i} {count}')

          
