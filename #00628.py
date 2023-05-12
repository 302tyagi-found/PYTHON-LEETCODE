# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        # product = 1
        # for i in range(0, 3):
        #     product *= nums[i]
        # max_product = abs(product)
        # for end in range(3, len(nums)):
        #     product /= nums[end - 3]
        #     product *= nums[end]
        #     max_product = max(max_product, product)
        # return int(max_product)
        max1, max2, max3, min1, min2 = float('-inf'), float('-inf'), float('-inf'), float('inf'), float('inf')
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(int(max3*max2*max1), int(min2*min1*max1))


sol = Solution()
nums = [-100, -98, -1, 2, 3, 4]
print(sol.maximumProduct(nums))
