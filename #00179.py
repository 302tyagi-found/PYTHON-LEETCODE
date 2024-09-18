# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of an integer.
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        # Convert all integers to strings for concatenation
        nums_str = list(map(str, nums))

        # Sort numbers using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))

        # Join the sorted list into one large number
        largest_num = ''.join(nums_str)

        # Edge case: if the result starts with "0", return "0"
        if largest_num[0] == '0':
            return '0'

        return largest_num
