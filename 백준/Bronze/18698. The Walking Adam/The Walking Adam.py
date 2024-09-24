# Read the number of test cases
T = int(input())

# Initialize a list to store results
results = []

# Process each test case
for _ in range(T):
    steps = input().strip()  # Read the step sequence
    count = 0  # Initialize count of steps before falling

    # Iterate over the steps
    for step in steps:
        if step == 'D':
            break  # Adam falls down, stop counting
        count += 1  # Increment count for 'U'

    # Append the result for this test case
    results.append(count)

# Print all results, each on a new line
for result in results:
    print(result)
