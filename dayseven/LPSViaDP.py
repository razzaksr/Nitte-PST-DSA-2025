def max_len_palindrome(sample, dna):
    rowSize = len(sample)
    colSize = len(dna)
    grid = [[0] * (colSize+1) for _ in range(rowSize+1)]
    for row in range(1,rowSize+1):
        for col in range(1,colSize+1):
            if sample[row-1] == dna[col-1]: 
                grid[row][col] = grid[row-1][col-1] + 1
            else:
                grid[row][col] = max(grid[row-1][col],grid[row][col-1])
    return grid[-1][-1]

pattern = "HLHLHHL"
print(max_len_palindrome(pattern,pattern[::-1]))
pattern = "HHLLHH"
print(max_len_palindrome(pattern,pattern[::-1]))
pattern = "HHHL"
print(max_len_palindrome(pattern,pattern[::-1]))