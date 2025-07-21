def findGridMinPath(grid):
    lenRow = len(grid)
    lenColumn = len(grid[0])
    # initialize 0th column of all row
    for row in range(1,lenRow): grid[row][0] += grid[row-1][0]
    # initialize all column of 0th row
    for column in range(1,lenColumn): grid[0][column] += grid[0][column-1]
    # find min
    for row in range(1,lenRow):
        for column in range(1, lenColumn):
            grid[row][column] += min(grid[row][column-1],grid[row-1][column])
    return grid[-1][-1]

print(findGridMinPath([[1,3,1],[1,5,1],[4,2,1]]))
print(findGridMinPath([[1,2],[1,1]]))
print(findGridMinPath([[5]]))
print(findGridMinPath([[1,2,3],[4,5,6]]))
print(findGridMinPath([[1,1,1],[1,1,1],[1,1,1]]))
