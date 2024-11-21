import sys
import math

def count_perfect_cubes(A, B):
    n_min = math.ceil(A ** (1/3))
    n_max = math.floor(B ** (1/3))
    if n_min > n_max:
        return 0
    return n_max - n_min + 1

def main():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        A, B = map(int, data[i].split())
        M = count_perfect_cubes(A, B)
        results.append(f"Case #{i}: {M}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
