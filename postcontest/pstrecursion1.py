def merge_two_lists(l1, l2):
    """Helper function to merge two sorted linked lists"""
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1[0] <= l2[0]:
        return [l1[0]] + merge_two_lists(l1[1:], l2)
    else:
        return [l2[0]] + merge_two_lists(l1, l2[1:])

def merge_k_sorted_lists(lists):
    """
    Merge k sorted linked lists using divide and conquer approach.
    Time Complexity: O(n log k) where n is total number of nodes
    Space Complexity: O(log k) for recursion stack
    """
    if not lists or len(lists) == 0:
        return []
    
    if len(lists) == 1:
        return lists[0]
    
    if len(lists) == 2:
        return merge_two_lists(lists[0], lists[1])
    
    mid = len(lists) // 2
    left = merge_k_sorted_lists(lists[:mid])
    right = merge_k_sorted_lists(lists[mid:])
    
    return merge_two_lists(left, right)
print(merge_k_sorted_lists([[1,4,5], [1,3,4], [2,6]]))
# import heapq
# def mergeAndSort(arr):
#     size=len(arr)
#     index=0
#     ans=[]
#     heapq.heapify(arr)
#     print(arr)
#     while index<size:
#         c_min_arr = heapq.heappop(arr)
#         ans.append(c_min_arr[0])
#         c_min_arr = c_min_arr[1:]
#         if c_min_arr!=[]: heapq.heappush(arr,c_min_arr)
#         else: index+=1
#     return ans
# arr=[[1,4,5], [1,3,4], [2,6]]
# print(mergeAndSort(arr))