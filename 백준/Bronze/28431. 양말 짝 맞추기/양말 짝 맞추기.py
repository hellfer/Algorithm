socks = [int(input().strip()) for _ in range(5)]

count = {}

for sock in socks:
    if sock in count:
        count[sock] += 1
    else:
        count[sock] = 1

for number, num_count in count.items():
    if num_count % 2 == 1: 
        print(number)
        break
