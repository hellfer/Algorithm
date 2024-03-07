n=input()
m=int(input())
result=[]
for _ in range(m):
    k=input()
    L=n.count('L')+k.count('L')
    O=n.count('O')+k.count('O')
    V=n.count('V')+k.count('V')
    E=n.count('E')+k.count('E')
    x=((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))%100
    result.append((-x, k))
result.sort()

print(result[0][1])
