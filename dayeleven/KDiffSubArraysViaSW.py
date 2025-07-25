from collections import defaultdict
# Count subarrays with at most k different integers
def count_subarrays_at_most_k(nums, k):
    count = defaultdict(int)
    left, total = 0, 0
    for right in range(len(nums)):
        count[nums[right]] += 1
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0: del count[nums[left]]
            left += 1
        total += right - left + 1
    return total
# Count subarrays with exactly k different integers
def subarrays_with_k_distinct(nums, k):
    return count_subarrays_at_most_k(nums, k) - count_subarrays_at_most_k(nums, k - 1)

print(subarrays_with_k_distinct([1, 2, 1, 2, 3], 2))  # Output: 7
print(subarrays_with_k_distinct([1, 2, 1, 3, 4], 3))  # Output: 3