import sys

N, M = map(int, sys.stdin.readline().split())

# 번호를 키로, 이름을 값으로 하는 딕셔너리
num_to_name = {}
# 이름을 키로, 번호를 값으로 하는 딕셔너리
name_to_num = {}

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    num_to_name[i] = name
    name_to_num[name] = i

for _ in range(M):
    query = sys.stdin.readline().strip()
    # query가 숫자인 경우
    if query.isdigit(): #문자열이 모두 숫자로 이루어져 있는지를 확인하는 함수
        print(num_to_name[int(query)]) # print('123'.isdigit()) 출력: True
    # query가 이름인 경우
    else:
        print(name_to_num[query])
