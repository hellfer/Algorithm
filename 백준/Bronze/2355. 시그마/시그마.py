A, B = map(int, input().split())
result = (A + B) * (abs(B - A) + 1) // 2
print(result)
