def multiply_matrix(X, Y):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += X[i][k] * Y[k][j]
    for i in range(2):
        for j in range(2):
            result[i][j] %= 1000000007
    return result

def power(matrix, b):
    if b == 1: return matrix
    elif b == 2: return multiply_matrix(matrix, matrix)
    elif b % 2 == 0: return power(multiply_matrix(matrix, matrix), b//2)
    else: return multiply_matrix(power(multiply_matrix(matrix, matrix), b//2), matrix)

n = int(input())
start_matrix = [[1, 1], [1, 0]]

if n == 1: print(1)
else:
    result_matrix = power(start_matrix, n-1)
    print(result_matrix[0][0] % 1000000007)




