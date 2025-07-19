def decoding(message):
    size = len(message)
    dynamic = [0] * (size+1)
    dynamic[0] = 1
    dynamic[1] = 1 if message[0]!="0" else 0
    for index in range(2,size+1):
        if message[index-1]!="0": dynamic[index] += dynamic[index-1]
        if 1<= int(message[index-2:index]) <= 26:
            dynamic[index] += dynamic[index-2]
    return dynamic[size]

print(decoding("226"))
print(decoding("2007"))
print(decoding("20007"))