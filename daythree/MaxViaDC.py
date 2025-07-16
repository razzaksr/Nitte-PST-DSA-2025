list=[0, 4, 5, 3, 7, 2, 1]
def findMaxBruteForce(i, high):
    if i==len(list):
        return high
    high=max(high,list[i])
    return findMaxBruteForce(i+1,high)
# print(findMaxBruteForce(0,float('-inf')))

def findMax(list):
    if len(list)==1:
        return list[0]
    return max(list[0],findMax(list[1:]))

print(findMax([900,20,450,210,60]))
print(findMax([0, 4, 5, 3, 7, 2, 1]))
print(findMax([20,10000,9.9,-10,0]))
print(findMax([-10,-100,-650,0,-200,-20,-3]))