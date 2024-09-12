# K/D/A 입력 받기
K, D, A = map(int, input().split('/'))

# 조건 검사
if K + A < D or D == 0:
    print('hasu')  # 가짜인 경우
else:
    print('gosu')  # 진짜인 경우

