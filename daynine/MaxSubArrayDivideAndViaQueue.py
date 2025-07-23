from collections import deque
# def minSumByAndSubarrays(nums, andValues):
#       n,m = len(nums), len(andValues)
#       if m>n:return -1
#       grid = [ [float('inf')] * (m+1) for _ in range(n+1) ]
#       grid[0][0] = 0
#       for i in range(1,n+1):
#             for j in range(1,m+1):
#                   and_accum = nums[i-1]
#                   for k in range(i-1,-1,-1):
#                         if k<i-1: and_accum &= nums[k]
#                         if and_accum == andValues[j-1]:
#                             grid[i][j] = min(grid[i][j],grid[k][j-1]+nums[i-1])
#       return grid[n][m] if grid[n][m] != float('inf') else -1

# def minSumByAndSubarrays(nums, andValues):
#       n,m = len(nums), len(andValues)
#       index = 0
#       que = deque()
#       for target in andValues:
#             found = False
#             value = nums[index]
#             for sub in range(index,n):
#                   value &= nums[sub]
#                   if value == target:
#                       que.append(nums[sub])
#                       index = sub+1
#                       found=True
#                       break
#             if not found: return -1
#       return sum(que)

# def minSumByAndSubarrays(nums, andValues):
#     n = len(nums)
#     m = len(andValues)
#     # dp[i] = minimum cost to use first i numbers
#     dp = [float('inf')] * (n + 1)
#     dp[0] = 0  # Start with 0 cost
#     # For each target AND value we need to match
#     for target in andValues:
#         new_dp = [float('inf')] * (n + 1)
#         # For each position in nums
#         for end in range(n):
#             # Use deque to store all possible AND values ending at this position
#             # Each item is (start_position, and_value)
#             possible_ands = deque()
#             # Calculate AND for all subarrays ending at 'end'
#             current_and = nums[end]
#             for start in range(end, -1, -1):
#                 if start < end: current_and &= nums[start]
#                 # Only keep if it could still match our target
#                 if current_and >= target: possible_ands.append((start, current_and))
#                 else: break  # AND will only get smaller, so stop
#             # Check if any subarray matches our target
#             for start_pos, and_val in possible_ands:
#                 if and_val == target:
#                     # We can use this subarray! Update our DP
#                     cost = dp[start_pos] + nums[end]
#                     new_dp[end + 1] = min(new_dp[end + 1], cost)
#         dp = new_dp
#     # Return result or -1 if impossible
#     return dp[n] if dp[n] != float('inf') else -1

def minSumByAndSubarrays(nums, andValues):
    currentSum = 0
    n,m = len(nums), len(andValues)
    available,pointer = nums[0], 0
    for index, element in enumerate(nums):
        available = element & available
        if pointer in range(m) and available == andValues[pointer]:
            currentSum+=element
            pointer+=1
            if index+1 < n: available = nums[index+1]
    return -1 if pointer<m else currentSum
# Test the function
print(minSumByAndSubarrays([4,6],[4]))
print(minSumByAndSubarrays([1,4,3,3,2], [0,3,3,2]))  
print(minSumByAndSubarrays([2,3,5,7,7,7,5], [0,7,5]))
print(minSumByAndSubarrays([1,2,3,4], [2]))
