n = int(input().strip())

for _ in range(n):
    sentence = input().strip()
    if not sentence.endswith('.'):
        sentence += '.'
    print(sentence)
