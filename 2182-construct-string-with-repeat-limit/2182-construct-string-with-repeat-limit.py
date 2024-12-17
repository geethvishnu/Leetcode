class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))
        
        result = []  
        while max_heap:
            current_char, current_count = heapq.heappop(max_heap)
            current_char = chr(-current_char)
            
            times_to_append = min(current_count, repeatLimit)
            result.append(current_char * times_to_append)
            
            current_count -= times_to_append
            
            if current_count > 0: 
                if not max_heap:
                    break 
                    
                next_char, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char)
                
                result.append(next_char)
                next_count -= 1  
                
                heapq.heappush(max_heap, (-ord(current_char), current_count))
                if next_count > 0:
                    heapq.heappush(max_heap, (-ord(next_char), next_count))
        
        return ''.join(result)

            