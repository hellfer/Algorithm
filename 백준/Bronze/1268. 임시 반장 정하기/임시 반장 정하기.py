n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
friends = [set() for _ in range(n)]

for grade in range(5):
    for i in range(n):
        for j in range(n):
            if i != j and classes[i][grade] == classes[j][grade]:
                friends[i].add(j)

max_friends = max(len(f) for f in friends)
for i in range(n):
    if len(friends[i]) == max_friends:
        print(i+1)
        break
