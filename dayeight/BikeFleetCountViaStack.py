def findFleetCount(target, position, speed):
    stack = []
    fleets = 0
    bikes=sorted(zip(position,speed),reverse=True)
    time = [(target-pos)/spd for pos,spd in bikes]
    # print(time)
    for current in time:
        if not stack or current > stack[-1]:
            fleets+=1
            stack.append(current)
    return fleets

print(findFleetCount(12,[10,8,0,5,3],[2,4,1,1,3]))
print(findFleetCount(10,[3],[3]))
print(findFleetCount(100,[0,2,4],[4,2,1]))