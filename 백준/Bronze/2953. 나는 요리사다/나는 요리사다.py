result = []
max_score = 0
winner = 0

for i in range(1, 6):
    scores = list(map(int, input().split()))
    total_score = sum(scores)
    result.append((i, total_score))
    if total_score > max_score:
        max_score = total_score
        winner = i

print(winner, max_score)
