T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    colors = list(map(int, input().split()))
    easiest_color = colors[0] 
    hardest_color = colors[N-1] 
    easiest_invalid = (easiest_color == X)
    hardest_invalid = (hardest_color == Y)
    if easiest_invalid and hardest_invalid:
        print("BOTH")
    elif easiest_invalid:
        print("EASY")
    elif hardest_invalid:
        print("HARD")
    else:
        print("OKAY")
