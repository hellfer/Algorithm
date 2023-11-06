n,m = map(int,input().split())
a = set()
for i in range(n):
    a.add(input())
b = set()
for j in range(m):
    b.add(input())
result = sorted(list(a&b))

print(len(result)) # 듣보잡의 수 출력
for i in result:
    print(i) # 듣보잡의 명단 출력
