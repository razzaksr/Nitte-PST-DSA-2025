def findPivot(packs, start, end):
    pivotData = packs[end]
    init = start-1
    # traversal
    for current in range(start,end):
        if packs[current] <= pivotData:
            init+=1
            packs[init],packs[current] = packs[current], packs[init]
    # always perform swap b/w init+1 and end
    packs[end],packs[init+1] = packs[init+1], packs[end]
    return init+1

def quickSelect(packs, top, start, end):
    if start==end: return packs[start]
    pivotalPoint = findPivot(packs,start, end)
    if pivotalPoint == top: return packs[pivotalPoint]
    elif pivotalPoint<top: 
        return quickSelect(packs,top,pivotalPoint+1,end)
    else: return quickSelect(packs,top,start,pivotalPoint-1)


# new approach
def quick_select(arr,k):
    if not arr : return None
    pivot=arr[0]
    left =[x for x in arr[1:] if x >= pivot]
    right =[x for x in arr[1:] if x <= pivot]
    l=len(left)
    if k <=l: return quick_select(left,k)
    elif k==l+1: return pivot
    else: return quick_select(right,k-l-1)

print(quick_select([14,23,7,15,20],5))    




# print(quickSelect(history,len(history)-2,0, len(history)-1))
# print(quickSelect(history,len(history)-3,0, len(history)-1))
# print(quickSelect(history,len(history)-1,0, len(history)-1))
# print(quickSelect(history,len(history)-4,0, len(history)-1))