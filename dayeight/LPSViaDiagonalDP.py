def findLPS(pattern):
    size = len(pattern)
    grid = [[0] * size for _ in range(size)]
    # fill length=1 diagonal as 1
    for i in range(size): grid[i][i] = 1
    # fill other diagonals
    for length in range(2,size+1):
        for index in range(size-length+1):
            compare = index+length-1
            if pattern[index] == pattern[compare] and length==2:
                grid[index][compare]=2
            elif pattern[index] == pattern[compare]:
                grid[index][compare] = grid[index+1][compare-1]+2
            else: 
                grid[index][compare] = max(grid[index+1][compare],
                                           grid[index][compare-1])
    return grid[0][-1]

print(findLPS("HHLLHH"))
print(findLPS("HLHLHHL"))
print(findLPS("HHHLL"))