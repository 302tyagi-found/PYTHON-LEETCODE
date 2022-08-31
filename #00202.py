# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:
        val = 0
        squared_sum = []
        if n == 1:
            return True
        else:
            while n != 1:
                for i in str(n):
                    val += int(i)**2
                    n = val
                squared_sum.append(val)
                if 1 in squared_sum:
                    return True
                elif squared_sum.count(val) > 1:
                    return False
                else:
                    val = 0
