N = int(input().strip())

for _ in range(N):
    angles = list(map(int, input().strip().split()))
    total = sum(angles)
    
    if total == 180:
        print(f"{angles[0]} {angles[1]} {angles[2]} Seems OK")
    else:
        print(f"{angles[0]} {angles[1]} {angles[2]} Check")
