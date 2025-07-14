def insertNewSlot(old,new):
    size = len(old)
    updated = []
    index = 0
    
    # add any non overlapping intervals before merging
    while index < size and old[index][1] < new[0]:
        updated.append(old[index])
        index+=1
    
    # merging
    while index < size and old[index][0] <= new[1]:
        new[0] = min(old[index][0],new[0])
        new[1] = max(old[index][1],new[1])
        index+=1
    updated.append(new)
    
    # add if any remaining
    while index < size:
        updated.append(old[index])
        index+=1
    
    return updated

print(insertNewSlot( [[1,3],[6,9]],[2,5]))
print(insertNewSlot( [[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))