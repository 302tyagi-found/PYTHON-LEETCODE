# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j
# should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.
class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        output = {}
        output_list = []
        least_common_string = ''
        least_common_index = float('inf')
        for i in range(len(list1)):
            index_sum = i
            if list1[i] in list2:
                index_sum += list2.index(list1[i])
                output[list1[i]] = index_sum
        for item, index in output.items():
            if index < least_common_index:
                least_common_index = index
                output_list = [item]
            elif index == least_common_index:
                output_list.append(item)
        return output_list
sol = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(sol.findRestaurant(list1, list2))
