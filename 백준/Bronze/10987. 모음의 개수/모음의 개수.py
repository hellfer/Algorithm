n=input()
x=['a','e','i','o','u']
count=0
for i in n:
    if i in x:
        count+=1
print(count)