nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def findmaxsubarray():
    # presum=0
    # high=0
    # for num in nums:
    #     presum+=num
    #     if presum<0:
    #         presum=0
    #     high=max(high,presum)
    # return high
    presum = nums[0]
    maxsum = nums[0]
    for num in nums[1:]:
        presum = max(num,presum+num)
        maxsum = max(presum,maxsum)
ans=findmaxsubarray()
print(ans)
            
    