def group_anagrams(strs):
    anagram_groups = {}
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)
    return list(anagram_groups.values())
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))