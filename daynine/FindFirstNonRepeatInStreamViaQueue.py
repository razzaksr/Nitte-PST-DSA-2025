from collections import deque
def find1stNonRepeat(stream):
    table = {}
    result = ""
    myQueue = deque()
    for char in stream:
        table[char] = table.get(char,0)+1
        myQueue.append(char)
        while myQueue and table[myQueue[0]] > 1: myQueue.popleft()
        result += myQueue[0] if myQueue else "#"
    return result
print(find1stNonRepeat("aabc"))
print(find1stNonRepeat("abcabc"))
print(find1stNonRepeat("aabbcc"))
print(find1stNonRepeat("xxyyz"))
print(find1stNonRepeat("abacabad"))

def solve(pattern):
    seen=set()
    queue=[]
    ans=""
    for char in pattern:
        if char not in seen:
            seen.add(char)
            queue.append(char)
        elif char == queue[0]:
            queue.pop(0)
        if queue: ans+=queue[0]
        else: ans+="#"
    return ans
print(solve("abacabad"))
print(solve("aabbcc"))