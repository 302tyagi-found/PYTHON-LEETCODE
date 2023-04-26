# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum = 0
            while num:
                sum += num % 10
                num = int(num // 10)
            num = sum
        return num
