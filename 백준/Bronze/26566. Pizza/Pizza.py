import math

# 데이터 세트 수 입력
n = int(input())

for _ in range(n):
    # 피자 조각의 면적과 가격 입력
    A1, P1 = map(int, input().split())
    
    # 원형 피자의 반경과 가격 입력
    R1, P2 = map(int, input().split())
    
    # 피자 조각의 면적당 가격
    value_slice = A1 / P1
    
    # 원형 피자의 면적 계산 (πR^2)
    area_pizza = math.pi * (R1 ** 2)
    # 원형 피자의 면적당 가격
    value_pizza = area_pizza / P2
    
    # 결과 비교 및 출력
    if value_slice > value_pizza:
        print("Slice of pizza")
    else:
        print("Whole pizza")
