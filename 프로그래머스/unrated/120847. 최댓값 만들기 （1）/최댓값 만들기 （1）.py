def solution(numbers):
    max1 = 0
    max2 = 0
    for i in range(len(numbers)):
        if numbers[i] > max1:
            max2 = max1
            max1 = numbers[i]
        elif numbers[i] > max2:
            max2 = numbers[i]
    return int(max1 * max2)
