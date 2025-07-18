def stairs(count):
    if count<1: return 0
    elif count == 1: return 1
    elif count == 2: return 2
    else:
        dynamic = [0] * (count+1)
        dynamic[0] = 0
        dynamic[1] = 1
        dynamic[2] = 2
        for index in range(3,count+1):
            dynamic[index] = dynamic[index-1]+dynamic[index-2]
        return dynamic[count]

print(stairs(5))
print(stairs(0))
print(stairs(1))
print(stairs(2))