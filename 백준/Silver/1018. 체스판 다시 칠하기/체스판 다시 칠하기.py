n,m=map(int,input().split())
x=[list(input()) for _ in range(n)]
result=[]

for i in range(n-7):
    for j in range(m-7):
        w,b=0,0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if x[k][l]!='W':w+=1
                    if x[k][l]!='B':b+=1
                else:
                    if x[k][l]!='W':b+=1
                    if x[k][l]!='B':w+=1
        result.append(w)
        result.append(b)
        
print(min(result))