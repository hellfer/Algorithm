numbers = list(map(int, input().strip().split()))

a, b, c = numbers

if a == b + c or b == a + c or c == a + b:
    print(1)

elif a == b * c or b == a * c or c == a * b:
    print(2)

else:
    print(3)
