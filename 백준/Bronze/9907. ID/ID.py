weights = [2, 7, 6, 5, 4, 3, 2]

nice_number = input().strip()

weighted_sum = 0
for i in range(7):
    digit = int(nice_number[i]) 
    weighted_sum += digit * weights[i]

remainder = weighted_sum % 11

mapping = ['J', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Z']
result_letter = mapping[remainder]

print(result_letter)
