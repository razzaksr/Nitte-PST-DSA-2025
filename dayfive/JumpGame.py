# def canJump(nums):
#     n = len(nums)
#     reach = 0
#     for i in range(n):
#         if i > reach:
#             break
#         reach = max(reach, i + nums[i])
#     return reach >= n - 1  


def canJump(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            return False
        i+=nums[i]
        if i==len(nums)-1:
            return True
    return False
    
print(canJump([2,3,1,1,4]))
print(canJump([1,1,0,1,4]))