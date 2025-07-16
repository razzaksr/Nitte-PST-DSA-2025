nums=[1,2,3,4,5]
k=9
def subarraySum():
    count=0
    presum=0
    d={}
    n=len(nums)
    for val in nums:
        presum+=val
        
        #check if presum=k
        if presum==k:
            count+=1
        if presum-k in d:
            count+=d[presum-k]
        
        d[presum]=1+d.get(presum,0)
    return count

print(subarraySum())
