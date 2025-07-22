def findMax(hist):
    hist.append(0) # fail safe for [2,4] since it gives 0 if we not add this
    stack = []
    maxArea = 0
    for index, value in enumerate(hist):
        while stack and hist[stack[-1]] > value:
            height = hist[stack.pop()]
            width = index if not stack else index - stack[-1] -1
            maxArea = max(maxArea,(height*width))
        stack.append(index)
    return maxArea

print(findMax([2,1,5,6,2,3])) # 10
print(findMax([2,4])) # 4