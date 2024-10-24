
Q = int(input())

problems_in_forum = 0
adios_declared = False

for _ in range(Q):
    event = input().strip().split()
    event_type = int(event[0])  # 1 or 2
    value = int(event[1])        # x or y

    if event_type == 1:
        problems_in_forum += value
    elif event_type == 2:
        if problems_in_forum < value:
            adios_declared = True
            break  
        else:
            problems_in_forum -= value

# Output the result
if adios_declared:
    print("Adios")
else:
    print("See you next month")
