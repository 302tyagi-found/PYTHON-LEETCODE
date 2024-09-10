# Given the head of a linked list head, in which each node contains an integer value.

# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

# Return the linked list after insertion.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        # Define a helper function to compute the GCD
        def gcd(a: int, b: int) -> int:
            return math.gcd(a, b)
        
        current = head
        
        while current and current.next:
            next_node = current.next
            gcd_value = gcd(current.val, next_node.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(gcd_value)
            
            # Insert the new node between current and next_node
            current.next = new_node
            new_node.next = next_node
            
            # Move to the next pair of nodes
            current = next_node
        
        return head