array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
T = int(input())
for i in range(1,T+1):
    x = list(input())
    count = 0
    for j in range(len(x)):
        if x[j] == array[j]:
            count += 1
        else:
            break
    print(f'#{i} {count}')


            
              