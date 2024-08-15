import math

x=int(input())

y=math.factorial(x)

count=0

z=str(y)

for i in range(len(z)):
    if z[i]=='0':
        count+=1
        
print(count)
