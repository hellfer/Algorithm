import math

def find_k(N):
    # 이차 방정식의 계수
    a = 1
    b = 1
    c = 1 - N

    # 판별식 계산
    discriminant = b ** 2 - 4 * a * c

    # K 계산
    k1 = (-b + math.isqrt(discriminant)) // (2 * a)
    k2 = (-b - math.isqrt(discriminant)) // (2 * a)

    # K는 양수이며 정수이므로, k1 또는 k2 중 양수인 것을 반환
    if k1 > 0:
        return k1
    else:
        return k2

# 입력 받기
N = int(input().strip())
print(find_k(N))