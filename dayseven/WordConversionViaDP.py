def convert(word1,word2):
    rowSize = len(word1)
    colSize = len(word2)
    grid = [[0] * (colSize+1) for _ in range(rowSize+1)]
    # initialize 0th column of all rows
    for row in range(rowSize+1): grid[row][0] = row
    # initialize all columns in 0th row
    for column in range(colSize+1): grid[0][column] = column
    for row in range(1,rowSize+1):
        for column in range(1,colSize+1):
            # copy diagonal if both are same
            if word1[row-1] == word2[column-1]:
                grid[row][column] = grid[row-1][column-1]
            else:
                grid[row][column] = 1+(min(grid[row-1][column-1],
                            min(grid[row-1][column],grid[row][column-1])))
    return grid[-1][-1]

print(convert("horse","rose"))
print(convert("help","elph"))