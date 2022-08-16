# Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        Reverse = 0
        y = x
        while(y > 0):
            Reminder = y % 10
            Reverse = (Reverse * 10) + Reminder
            y = y // 10
        if x == Reverse:
            return True
        else:
            return False


print(Solution.isPalindrome(self=True, x=126))
