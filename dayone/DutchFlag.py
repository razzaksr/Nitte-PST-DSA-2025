def sortByDutch(arr):
    left = index = 0
    right = len(arr)-1
    
    while index <= right:
        # 0's
        if arr[index] == 0:
            arr[left],arr[index] = arr[index], arr[left]
            index+=1
            left+=1
        elif arr[index] == 1:
            index+=1
        else:
            arr[right],arr[index] = arr[index], arr[right]
            right-=1
    print(arr)
    
sortByDutch([2,0,0,1,0,2,0,1])
sortByDutch([2, 0, 2, 1, 1, 0])