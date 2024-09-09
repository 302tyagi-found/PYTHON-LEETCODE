// Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

// The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

/// The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

// Return an array of the k parts.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Calculate the base size of each part and the number of parts that need to be larger
        base_size = length // k
        extra_parts = length % k
        
        # Step 3: Split the list into k parts
        parts = []
        current = head
        for i in range(k):
            part_size = base_size + (1 if i < extra_parts else 0)
            if part_size == 0:
                parts.append(None)
            else:
                parts.append(current)
                # Move current to the end of the current part
                for _ in range(part_size - 1):
                    current = current.next
                # Break the list
                next_head = current.next
                current.next = None
                current = next_head
        
        return parts 