bits = list(map(int, input().split()))

if all(bit != 9 for bit in bits):
    print("S")
else:
    print("F")
