n = int(input())
team_names = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
result = []

for i in range(9):
    scores = list(map(int, input().split()))
    result.append((max(scores), team_names[i]))

result.sort(reverse=True)
print(result[0][1])
