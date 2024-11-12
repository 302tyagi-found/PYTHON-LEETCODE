# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.
#
# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.
#
# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.
#
#
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price (first element in each sublist)
        items.sort()

        # Precompute the maximum beauty at each price level
        max_beauty_at_price = []
        current_max_beauty = 0

        for price, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            max_beauty_at_price.append((price, current_max_beauty))

        # Sort queries with indices to map results back to original order
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        # Prepare result array
        result = [0] * len(queries)

        # Process each query
        for query, original_index in sorted_queries:
            # Binary search to find the largest price <= query
            idx = bisect_right(max_beauty_at_price, (query, float('inf'))) - 1
            if idx >= 0:
                result[original_index] = max_beauty_at_price[idx][1]
            else:
                result[original_index] = 0

        return result