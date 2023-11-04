def solution(n):
    result1 = []
    result2 = []
    for i in range(1, n+1):
        if i % 2 != 0:
            result1.append(i)
        else:
            result2.append(i*i)
    if n % 2 != 0:
        return sum(result1)
    else:
        return sum(result2)

            