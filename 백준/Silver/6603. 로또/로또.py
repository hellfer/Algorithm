import itertools

while True:
    n=list(map(int,input().split()))
    
    if n[0]==0:
        break
    
    for i in itertools.combinations(n[1:] , 6):
        print(*i)
    print()