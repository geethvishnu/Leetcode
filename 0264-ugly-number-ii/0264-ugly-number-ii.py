import heapq
import math
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        seen = {1}
    
        for _ in range(n):

            current = heapq.heappop(heap)
        
            for factor in [2, 3, 5]:
                new_ugly = current * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
    
        return current