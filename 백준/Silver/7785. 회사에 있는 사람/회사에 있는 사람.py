# 입력받을 사람의 수
n = int(input())

# 회사에 있는 사람들의 명단을 저장할 set
company = set()

for _ in range(n):
    # 이름과 출입 여부를 입력받음
    name, status = input().split()
    if status == 'enter':
        # 출입 여부가 'enter'이면 회사에 있는 사람들의 명단에 추가
        company.add(name)
    else:
        # 출입 여부가 'leave'이면 회사에 있는 사람들의 명단에서 제거
        company.remove(name)

# 회사에 남아있는 사람들의 명단을 사전 순으로 역순 정렬
people = sorted(list(company), reverse=True)

# 결과 출력
for person in people:
    print(person)
