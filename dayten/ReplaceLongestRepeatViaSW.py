from collections import defaultdict
def character_replacement(s, k):
    count = defaultdict(int)
    max_freq, left, longest = 0, 0, 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        # If current window size minus max_freq exceeds k, shrink from left
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest

# Example usage
print(character_replacement("ABAB", 2))      # Output: 4
print(character_replacement("AABABBA", 1))   # Output: 4