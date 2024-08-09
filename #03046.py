# You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:
#
# nums1.length == nums2.length == nums.length / 2.
# nums1 should contain distinct elements.
# nums2 should also contain distinct elements.
# Return true if it is possible to split the array, and false otherwise.
from typing import List


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        class Solution:
            def isPossibleToSplit(self, nums: List[int]) -> bool:
                count = {}

                for n in nums:
                    count[n] = 1 + count.get(n, 0)

                for val in count.values():
                    if val > 2:
                        return False

                return True
