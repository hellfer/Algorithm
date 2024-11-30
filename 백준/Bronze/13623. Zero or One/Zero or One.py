# 입력을 받는다
A, B, C = map(int, input().split())

# 승자 결정
if A == B == C:
    print('*')  # 모두 같은 경우
elif A != B and A != C:
    print('A')  # Alice가 승자
elif B != A and B != C:
    print('B')  # Bob이 승자
elif C != A and C != B:
    print('C')  # Clara가 승자
else:
    print('*')  # 승자가 없는 경우
