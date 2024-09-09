# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)
        ans = ListNode(0)
        tail = ans

        while head:
            val = head.val
            head = head.next
            if val not in nums:
                tail.next = ListNode(val)
                tail = tail.next
        return ans.next
