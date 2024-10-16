def knight_can_reach(n, r1, c1, r2, c2):
    knight_moves = [
        (r1 + 2, c1 + 1),
        (r1 + 2, c1 - 1),
        (r1 - 2, c1 + 1),
        (r1 - 2, c1 - 1),
        (r1 + 1, c1 + 2),
        (r1 + 1, c1 - 2),
        (r1 - 1, c1 + 2),
        (r1 - 1, c1 - 2)
    ]
    
    for move in knight_moves:
        if move == (r2, c2):
            return "YES"
    
    return "NO"

T = int(input())
for case_number in range(1, T + 1):
    n, r1, c1, r2, c2 = map(int, input().split())
    result = knight_can_reach(n, r1, c1, r2, c2)
    print(f"Case {case_number}: {result}")
