def decode(received):
    size = len(received)
    dynamic = [0] * (size + 1)
    dynamic[0] = 1
    dynamic[1] = 0 if received[0] == "0" else 1
    for index in range(2, size + 1):
        if received[index-1] != "0":
            dynamic[index] += dynamic[index-1]
        if 10 <= int(received[index-2:index]) <= 26:
            dynamic[index] += dynamic[index-2]
    return dynamic[size]  # Output: 3

print(decode("226"))
