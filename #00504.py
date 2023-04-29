# Given an integer num, return a string of its base 7 representation.
class Solution:
    def convertToBase7(self, num: int) -> str:
        digits = []
        negative = False
        if num == 0:
            return '0'
        if num < 0:
            negative = True
            num = abs(num)
        while num > 0:
            digits.append(num%7)
            num //= 7
        digits.reverse()
        result = ''.join(str(d) for d in digits)
        if negative:
            result = '-' + result
        return result