def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b = map(int, input().split())
c, d = map(int, input().split())

x = lcm(b, d)  # 공통 분모
y = a * (x // b) + c * (x // d)  # 분자

# 최종 결과를 기약분수 형태로 만듦
g = gcd(y, x)
y //= g
x //= g

print(y, x)
