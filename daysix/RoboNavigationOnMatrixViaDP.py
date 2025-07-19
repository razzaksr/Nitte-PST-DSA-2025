def maxToReachDown(row, column):
    # if row!=column: return 0
    dyn = [[1] * column for _ in range(row)]
    for nav_r in range(1,row):
        for nav_c in range(1,column):
            dyn[nav_r][nav_c] = dyn[nav_r-1][nav_c]+dyn[nav_r][nav_c-1]
    return dyn[-1][-1]
print(maxToReachDown(3,3))
print(maxToReachDown(2,2))
print(maxToReachDown(1,5))
print(maxToReachDown(4,3))
print(maxToReachDown(4,1))