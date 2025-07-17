def secureRob(house_values, index=0):
    if index >= len(house_values): return 0
    # Choice 1: Monitor current house + skip next
    current = house_values[index] + secureRob(house_values, index + 2)
    # Choice 2: Skip current house
    skip_current = secureRob(house_values, index + 1)        
    return max(current, skip_current)

print(secureRob([500, 100, 300, 400, 200]))
print(secureRob([500, 400, 300, 200]))
print(secureRob([500, 400, 300, 200, 100]))
print(secureRob([500, 100, 300, 400]))
print(secureRob([1,-20,-20,-20,2]))

# houses=[500,100,300,400,200]
# maxamount=0
# def Rob(i,amount):
#     if i>=len(houses):
#         return amount
#     maxamount=max(Rob(i+1,amount),Rob(i+2,amount+houses[i]))
#     return maxamount
# print(Rob(0,0))

