# result = []
# def genBrackets(limit,current='', open_count=0, close_count=0):
#     if len(current) == 2 * limit:
#         result.append(current)
#         return
#     if open_count < limit:
#         genBrackets(limit,current + '(', open_count + 1, close_count)
#     if close_count < open_count:
#         genBrackets(limit,current + ')', open_count, close_count + 1)
        
# genBrackets(3)
# print(result)
# result = []
# genBrackets(2)
# print(result)
# genBrackets(4)
# print(result)




def getAllPaterns(n,pattern=''):
    n_open = pattern.count('(')
    n_close = pattern.count(')')
    if n_close == n:
        return [pattern]
    
    ans=[]
    if n_open<n:
        ans+=getAllPaterns(n,pattern+"(")
    if n_close<n_open:
        ans+=getAllPaterns(n,pattern+")")
    return ans

print(getAllPaterns(3))