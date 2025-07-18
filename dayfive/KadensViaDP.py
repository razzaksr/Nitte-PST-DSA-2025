def findSubMax(numbers):
    size = len(numbers)
    dynmaic = [0] * size
    dynmaic[0] = numbers[0]
    for index in range(1, size):
        dynmaic[index] = max(numbers[index], dynmaic[index-1] + numbers[index])
    print(dynmaic)
    return max(dynmaic)

print(findSubMax([-2,1,-3,4,-1,2,1,-5,4]))