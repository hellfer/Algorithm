N = int(input())
S = input().strip()

result = []

for i in range(N - 1):
    if S[i + 1] == 'J':
        result.append(S[i])

print("\n".join(result))
