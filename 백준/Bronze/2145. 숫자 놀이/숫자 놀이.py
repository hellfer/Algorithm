while True:
    N = input()
    if N == '0':
        break
    
    # 숫자를 계속 더하여 한 자릿수가 될 때까지 반복
    while len(N) > 1:
        N = str(sum(int(digit) for digit in N))  # 각 자릿수를 더한 후 문자열로 변환
    
    print(N)
