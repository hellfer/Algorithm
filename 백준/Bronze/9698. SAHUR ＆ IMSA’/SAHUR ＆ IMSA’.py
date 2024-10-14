# 입력받기
T = int(input())

# 각 테스트 케이스에 대해 처리
for case_number in range(1, T + 1):
    H, M = map(int, input().split())
    
    # 45분 전으로 계산
    M -= 45
    if M < 0:
        M += 60
        H -= 1
        if H < 0:
            H += 24
    
    # 결과 출력
    print(f"Case #{case_number}: {H} {M}")