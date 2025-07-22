def check(pattern):
    stack=[]
    for bracket in pattern:
        if bracket in "]})" and not stack:
            return False
        if bracket in "({[":
            stack.append(bracket)
        elif bracket==")" and stack[-1]=="(":
            stack.pop()
        elif bracket=="}" and stack[-1]=="{":
            stack.pop()
        elif bracket=="]" and stack[-1]=="[":
            stack.pop()
    if stack: return False
    else: return True

# def check(expression):
#     table = {'}':'{',')':'(',']':'['}
#     stack = []
#     for char in expression:
#         if char in table.values(): stack.append(char)
#         elif char in table.keys(): 
#             if not stack or table[char] != stack[-1]: 
#                 return False
#             stack.pop()
#     return True if not stack else False
    
print(check("(){}[]"))
print(check("([)]"))
print(check("][]"))
print(check("(]"))
print(check("([])"))
print(check("()"))