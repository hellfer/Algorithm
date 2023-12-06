def check(num):
    if num==1:
        False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
n=int(input())
x=list(map(int,input().split()))
count=0

for i in x:
    if check(i):
        count+=1
        
print(count)