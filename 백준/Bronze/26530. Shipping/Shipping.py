n = int(input())

for _ in range(n):
    x = int(input())
    
    total_revenue = 0.0
    
    for _ in range(x):
        line = input().split()
        item_name = line[0] 
        quantity = int(line[1])
        unit_price = float(line[2])
        total_revenue += quantity * unit_price
    
    print(f"${total_revenue:.2f}")
