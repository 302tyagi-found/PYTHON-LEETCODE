# There is a function signFunc(x) that returns:
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).
class Solution:
    def arraySign(self, nums: list[int]) -> int:
        # product = 1
        # for i in nums:
        #     product *= i
        # if product < 0:
        #     return -1
        # elif product > 0:
        #     return 1
        # else:
        #     return 0

        # or

        sign = 1
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                sign = -sign
        return sign