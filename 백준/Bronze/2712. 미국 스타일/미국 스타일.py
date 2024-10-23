def convert(value, unit):
    if unit == 'kg':
        return value * 2.2046, 'lb'  
    elif unit == 'lb':
        return value * 0.4536, 'kg' 
    elif unit == 'l':
        return value * 0.2642, 'g'   
    elif unit == 'g':
        return value * 3.7854, 'l'
    else:
        raise ValueError("Invalid unit")

T = int(input())

for _ in range(T):
    line = input().strip().split()
    value = float(line[0]) 
    unit = line[1]     

    converted_value, converted_unit = convert(value, unit)

    print(f"{converted_value:.4f} {converted_unit}")
