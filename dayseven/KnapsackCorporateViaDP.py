def maxProfit(project, cost, capacity):
    rowSize = len(project)
    colSize = capacity+1
    grid = [[0] * colSize for _ in range(rowSize+1)]
    for row in range(1,rowSize+1):
        for col in range(1, colSize):
            # find max
            if project[row-1] <= col:
                grid[row][col] = max(grid[row-1][col],
                grid[row-1][col - project[row-1]]+cost[row-1])
            else:
                grid[row][col] = grid[row-1][col]
    return grid[-1][-1]


# Space optimization
def maxProfit2(projects, costs, capacity):
    size = capacity+1
    prvs = [0]*size
    crr = [0]*size
    
    for project,cost in zip(projects,costs):
        for i in range(project,size):
            crr[i] = max(crr[i],prvs[i-project] + cost)
        for i in range(size):
            prvs[i] =crr[i]
    return crr[-1]
    
print(maxProfit2([1,2,3],[10,15,40],5))
print(maxProfit2([1,3,4,5],[10,40,50,70],8))
print(maxProfit2([1,2,3,2],[10,20,30,40],5))