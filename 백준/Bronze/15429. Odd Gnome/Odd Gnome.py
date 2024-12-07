n = int(input())

results = []

for _ in range(n):
    data = list(map(int, input().split()))
    g = data[0] 
    gnomes = data[1:]  
    king_position = -1
    for i in range(1, g - 1):
        if gnomes[i] != gnomes[i - 1] + 1:
            king_position = i + 1
            break
    results.append(king_position)

for result in results:
    print(result)
