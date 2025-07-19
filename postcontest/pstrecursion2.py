# def find_max_occurence(arr):
#     c_ele=arr[0]
#     c_count=1
#     for ele in arr[1:]:
#         if c_count == 0:
#             c_ele=ele
#             c_count=1
#             continue
#         if c_ele == ele:
#             c_count+=1
#         else:
#             c_count-=1
#     return c_ele

# arr = [1,1,2,2,2,1,1]
# print(find_max_occurence(arr))
def findMajority(nums):
    if len(nums) == 1: return nums[0]
    mid = len(nums) // 2
    left_majority = findMajority(nums[:mid])
    right_majority = findMajority(nums[mid:])
    if left_majority == right_majority: return left_majority
    left_count = nums.count(left_majority)
    right_count = nums.count(right_majority)
    if left_count > right_count: return left_majority
    else: return right_majority

print(findMajority([2,2,1,1,1,2,2]))
print(findMajority([1,1,1,2,3,4,1]))