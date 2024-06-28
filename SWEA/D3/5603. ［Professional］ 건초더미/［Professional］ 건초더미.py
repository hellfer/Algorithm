# 테스트 케이스의 개수를 입력받습니다.
T = int(input())

for tc in range(1, T + 1):
    # 건초더미의 개수를 입력받습니다.
    N = int(input())
    
    # 모든 건초더미의 크기를 입력받아 리스트에 저장합니다.
    haystacks = []
    for _ in range(N):
        haystacks.append(int(input()))
    
    # 건초더미의 총합을 계산합니다.
    total_hay = sum(haystacks)
    
    # 각 건초더미의 크기를 같게 만들기 위한 목표 크기는 평균입니다.
    target_hay = total_hay // N
    
    # 최소 이동 횟수를 계산합니다.
    moves = 0
    for hay in haystacks:
        if hay > target_hay:
            moves += hay - target_hay
    
    # 결과를 출력합니다.
    print(f'#{tc} {moves}')

