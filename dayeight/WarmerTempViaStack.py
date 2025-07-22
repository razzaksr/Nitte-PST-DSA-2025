def findNextWarmerDay(temperatures):
    size = len(temperatures)
    result = [0] * size
    stack = []
    for index in range(size):
        while stack and temperatures[index] > temperatures[stack[-1]]:
            popped = stack.pop()
            result[popped] = index - popped
        stack.append(index)
    return result
print(findNextWarmerDay([73,74,75,71,69,72,76,73]))
print(findNextWarmerDay([30,40,50,60]))
print(findNextWarmerDay([30,60,90]))