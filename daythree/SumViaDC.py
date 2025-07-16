def sumArray(nums):
    if not nums:
        return 0
    return nums[0] + sumArray(nums[1:])

print(sumArray([900,20,450,210,60]))