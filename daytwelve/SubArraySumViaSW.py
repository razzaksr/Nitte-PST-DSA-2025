# time complexity: O(n*w)
# def subarray(myList,window):
#     if not myList: None
#     # myList = []
#     newList = [0] * (len(myList)-window+1)
#     for index in range(0,len(myList)-window+1):
#     #    newList.append(sum(myList[index:(index+window)]))
#         newList[index] = sum(myList[index:(index+window)])
#     return newList
# print(subarray([7,3,1,4,2,8,3],3))

# time complexity: O(n)
def subarray(myList,window):
    newlist = []
    currentSum = 0
    for each in myList[:window]: currentSum+=each
    newlist.append(currentSum)
    for index in range(len(myList)-window):
        currentSum -= myList[index]
        currentSum += myList[index+window]
        newlist.append(currentSum)
    return newlist
print(subarray([7,3,1,4,2,8,3],3))