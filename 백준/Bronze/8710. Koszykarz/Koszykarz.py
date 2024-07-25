x,y,z=map(int,input().split())

if (y-x)%z==0:
    print(((y-x)//z))
else:
    print(((y-x)//z)+1)