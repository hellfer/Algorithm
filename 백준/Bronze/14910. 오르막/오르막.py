x=list(map(int,input().split()))
count=1
for i in range(len(x)-1):
    if x[i]<=x[i+1]:
        count+=1
        
if count==len(x):
    print('Good')
else:
    print('Bad')