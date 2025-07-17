phone = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}
result = []
def findCombinations(digits, index, current_combination):
    if not digits: return []
    if index == len(digits):
        result.append(current_combination)
        return
    for letter in phone[digits[index]]:
        findCombinations(digits,index + 1, current_combination + letter)
findCombinations("23",0,'')
print(result)
result=[]
findCombinations("729",0,'')
print(result)
result=[]
findCombinations("6642633",0,'')
print(result)


# def solve(num):
#     ans=[]
#     if num in phone:
#         for i in phone[num]:
#             ans.append(i)
#         return ans
#     for digit in phone[num[0]]:
#         for j in solve(num[1:]):
#             ans.append(digit+j)
#     return ans

# print(solve("2"))
# print(solve("23"))