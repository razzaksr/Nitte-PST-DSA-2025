# using sliding window to find minimum sub string on customer analysis of ecommerce
def findMinSub(current,freequent):
    freequent_table = {}
    for action in freequent: freequent_table[action] = freequent_table.get(action,0)+1
    minLength = float("inf")
    start, matched, minStart, current_table = 0, 0, 0, {}
    # extending the window
    for end in range(len(current)):
        action = current[end]
        current_table[action] = current_table.get(action,0)+1
        if freequent_table.get(action,0)>0: matched+=1
        # shrink the window
        while matched == len(freequent_table):
            if end-start+1 <= minLength:
                minLength = end-start+1
                minStart = start
            action = current[start]
            if current_table.get(action,0)>0: 
                current_table[action]=current_table.get(action)-1
                if freequent_table.get(action,0)>0: matched-=1
            start+=1
    return current[minStart:(minStart+minLength)]

print(findMinSub(
        ["browse", "search product", "add to cart", "checkout", "feedback"],
        ["search product", "checkout"]
    )
)