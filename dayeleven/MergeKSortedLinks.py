def create_node(val): return {'val': val, 'next': None}

def build_linked_list(arr):
    if not arr: return None
    head = create_node(arr[0])
    current = head
    for val in arr[1:]:
        current['next'] = create_node(val)
        current = current['next']
    return head

def merge_two_lists(left, right):
    dummy = create_node(0)
    tail = dummy
    while left and right:
        if left['val'] < right['val']:
            tail['next'] = left
            left = left['next']
        else:
            tail['next'] = right
            right = right['next']
        tail = tail['next']
    tail['next'] = left if left else right
    return dummy['next']

def merge_k_lists(lists):
    if not lists: return None
    while len(lists) > 1:
        merged = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            merged.append(merge_two_lists(l1, l2))
        lists = merged
    return lists[0]
def traverse(node):
    while node:
        print(node['val'],end=" -> ")
        node = node['next']
    print("N")
    
lists = [
    build_linked_list([1, 4, 5]),build_linked_list([1, 3, 4]),
    build_linked_list([2, 6])
]
merged = merge_k_lists(lists)
traverse(merged)  # Output: [1, 1, 2, 3, 4, 4, 5, 6]