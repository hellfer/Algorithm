n=input()

m=len(n)

y=set()

for i in range(m):
    for j in range(i+1,m+1):
        y.add(n[i:j])

print(len(y))