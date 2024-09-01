x=int(input())
t=input()

count1=0
count2=0
for i in t:
    if i=='A':
        count1+=1
    if i=='B':
        count2+=1

if count1==count2:
    print('Tie')
elif count1>count2:
    print('A')
else:
    print('B')