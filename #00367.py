# Given a positive integer num, return true if num is a perfect square or false otherwise.
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
# You must not use any built-in library function, such as sqrt.
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i <= num:
            if i * i == num:
                return True
            i += 1
        return False

        # or
        
        if num == 1:
            return True
        else:
            left = 0
            right = num
            while left < right:
                mid = (left + right) // 2
                if mid * mid == num:
                    return True
                elif mid * mid > num:
                    right = mid
                else:
                    left = mid + 1
            return False

