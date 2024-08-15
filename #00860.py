# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
#
# Note that you do not have any change in hand at first.
#
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
#
#
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_count = ten_dollar_count = twenty_dollar_count = 0
        for bill in bills:
            if bill == 5:
                five_dollar_count += 1
            elif bill == 10:
                if five_dollar_count < 1:
                    return False
                else:
                    five_dollar_count -= 1
                    ten_dollar_count += 1
            elif bill == 20:
                if five_dollar_count < 3 and ten_dollar_count < 1:
                    return False
                elif five_dollar_count < 1:
                    return False
                elif ten_dollar_count < 1 and five_dollar_count > 3:
                    five_dollar_count -= 3
                    twenty_dollar_count += 1
                else:
                    five_dollar_count -= 1
                    ten_dollar_count -= 1
                    twenty_dollar_count += 1
        return True


sol = Solution()
bills = [5, 5, 5, 10, 5, 5, 10, 20, 20, 20]
print(sol.lemonadeChange(bills))
