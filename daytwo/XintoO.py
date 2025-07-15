def findCount(board):
    count = index = 0
    while index<len(board):
        if board[index] == 'X':
            index+=3
            count+=1
        else:index+=1
    return count

print(findCount("XXOX"))
print(findCount("XXX"))
print(findCount("OOOO"))