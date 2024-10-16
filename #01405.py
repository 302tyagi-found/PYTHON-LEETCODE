# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max-heap based on the counts of 'a', 'b', 'c'
        max_heap = []
        if a > 0: heapq.heappush(max_heap, (-a, 'a'))
        if b > 0: heapq.heappush(max_heap, (-b, 'b'))
        if c > 0: heapq.heappush(max_heap, (-c, 'c'))

        happy_string = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            count = -count  # Convert back to positive count

            # If the last two characters in happy_string are the same as char,
            # we can't add char without forming "xxx"
            if len(happy_string) >= 2 and happy_string[-1] == char and happy_string[-2] == char:
                # If we can't add the current char, check the next character in the heap
                if not max_heap:
                    break  # No more characters can be added
                next_count, next_char = heapq.heappop(max_heap)
                next_count = -next_count

                # Add the next character if it's available
                happy_string.append(next_char)
                next_count -= 1

                # Push the next character back into the heap if there's still some left
                if next_count > 0:
                    heapq.heappush(max_heap, (-next_count, next_char))

                # Push the current character back into the heap as well
                heapq.heappush(max_heap, (-count, char))
            else:
                # Add the current character to the happy string
                happy_string.append(char)
                count -= 1

                # Push the character back into the heap if there's still some left
                if count > 0:
                    heapq.heappush(max_heap, (-count, char))

        return ''.join(happy_string)
