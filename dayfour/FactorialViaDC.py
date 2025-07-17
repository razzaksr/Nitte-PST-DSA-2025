def findFact(num):
    if num <= 1: return 1
    else: return num*findFact(num-1)

print(findFact(5))
print(findFact(7))
print(findFact(0))
print(findFact(8))
print(findFact(10))