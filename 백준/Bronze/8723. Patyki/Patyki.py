def can_form_triangle(a, b, c):
    # 변의 길이를 정렬
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]
    
    # 직각삼각형 확인
    is_right_triangle = (a * a + b * b == c * c)
    
    # 정삼각형 확인
    is_equilateral_triangle = (a == b == c)
    
    if is_equilateral_triangle:
        return 2  # 정삼각형
    elif is_right_triangle:
        return 1  # 직각삼각형
    else:
        return 0  # 둘 다 아님

# 입력 처리
a, b, c = map(int, input().split())

# 결과 출력
print(can_form_triangle(a, b, c))
