from itertools import combinations

# 함수를 만들어서 자음 모음 검사를 합니다.
def check(password):
    mo = 0
    ja = 0
    for i in password:
        if i in ['a', 'e', 'i', 'o', 'u']:
            mo += 1
        else:
            ja += 1
    return mo >= 1 and ja >= 2

# 입력을 받습니다.
L, C = map(int, input().split())
array = input().split()
array.sort()

# 가능한 모든 경우의 수를 조합을 이용해서 만듭니다.
for password in combinations(array, L):
    # 만약 자음 모음 검사를 통과한다면 출력합니다.
    if check(password):
        print(''.join(password))
