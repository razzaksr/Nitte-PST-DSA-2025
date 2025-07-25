class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseKGroup(head, k):
    # Dummy node to simplify edge handling
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy
    while True:
        # Find the kth node
        kth = prev_group_end
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next  # Fewer than k nodes remain
        next_group_start = kth.next  # Save start of next group
        # Reverse k nodes
        prev, curr = None, prev_group_end.next
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Connect with previous and next parts
        start = prev_group_end.next
        prev_group_end.next = prev
        start.next = next_group_start
        prev_group_end = start  # Move to the end of the newly reversed group
    return dummy.next
def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

# Test
head = build_linked_list([1,2,3,4,5])
k = 2
new_head = reverseKGroup(head, k)
print_linked_list(new_head)  # Output: [2,1,4,3,5]