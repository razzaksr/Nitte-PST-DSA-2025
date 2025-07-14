def findPivot(arr):
    total_sum = sum(arr)
    part_sum = 0
    
    for index,value in enumerate(arr):
        if part_sum == total_sum - part_sum -value:
            return index
        part_sum+=value
    return -1

print(findPivot([1, 7, 3, 6, 5, 6]))
print(findPivot([-7, 1, 5, 2, -4, 3, 0]))
print(findPivot([0,-3,5,-4,-2,3,1,0]))