def clock_hand_position(A, B):
    # Calculate new position using modulo arithmetic
    new_position = (A + B - 1) % 12 + 1
    return new_position

def main():
    import sys
    # Reading inputs
    A = int(sys.stdin.readline().strip())
    B = int(sys.stdin.readline().strip())
    
    result = clock_hand_position(A, B)
    print(result)

if __name__ == "__main__":
    main()
