n=int(input())

for i in range(n):
    x=input()
    result=""
    for j in x:
        if not result or j != result[-1]:
            result+=j
    print(result)