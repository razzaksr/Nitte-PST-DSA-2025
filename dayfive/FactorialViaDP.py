def findFact(number):
    if number <= 0: return -1
    else:
        dynamic = [0] * (number+1)
        dynamic[0] = 1
        for index in range(1,number+1):
            dynamic[index] = dynamic[index-1] * index
    return dynamic[number]

print(findFact(5))
print(findFact(-1))
print(findFact(1))
print(findFact(7))