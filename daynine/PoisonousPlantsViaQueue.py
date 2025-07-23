from collections import deque
def findDayPlantsNoDie(plants):
    size = len(plants)
    grid = [0] * size
    maxDay = 0
    que = deque()
    for index in range(size):
        while que and plants[index] <= plants[que[-1]]: que.pop()
        if que: grid[index] = grid[que[-1]] + 1
        else: grid[index] = 0
        que.append(index)
        maxDay = max(maxDay, grid[index])
    return maxDay
print(findDayPlantsNoDie([6,5,8,4,7,10,9]))