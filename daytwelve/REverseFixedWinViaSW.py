# time complexity: O(n*w)
def reverse(mylist, window):
    if not mylist: return None
    newList = []
    for index in range(0,len(mylist),window):
        # slicing to build cluster
        cluster = mylist[index:(index+window)]
        if len(cluster) == window: newList.extend(cluster[::-1])
        else: newList.extend(mylist[index:])
    return newList
# print(reverse([4,9,7,6,2],2))



