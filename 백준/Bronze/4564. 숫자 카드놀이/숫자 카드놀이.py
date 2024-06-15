def check(n):
    result=[n]
    while len(n) != 1:
        product = 1
        for digit in n:
            product *= int(digit)
        n = str(product)
        result.append(n)
    return result

while True:
    x = input()
    if x == '0':
        break
    y = check(x)
    print(' '.join(y))