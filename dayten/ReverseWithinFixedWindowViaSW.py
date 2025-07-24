# reverse the list with given window size

def reverseWindow(myList,myWindow):
    myOutCome = []
    for index in range(0,len(myList),myWindow):
        cluster = myList[index:(index+myWindow)]
        if myWindow == len(cluster):
            myOutCome.extend(cluster[::-1])
        else:
            myOutCome.extend(cluster)
    return myOutCome

print(reverseWindow([1, 2, 3, 4, 5],3))
print(reverseWindow([1, 2, 3, 4, 5],2))