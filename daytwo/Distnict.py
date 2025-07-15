def findDistnict(numbers):
    whole_string = ""
    for each in numbers: whole_string += str(each)
    print(sorted(set(whole_string)))
    
    # bool_arr = [False] * 10
    # for each in numbers:
    #     while each>0:
    #         bool_arr[int(each%10)]=True
    #         each//=10
    # for index,each in enumerate(bool_arr):
    #     if each==True:print(index,end=" ")
    # print()
    

findDistnict([131, 11, 48])
findDistnict([111, 222, 333, 4444, 666])
findDistnict([98, 67, 91])