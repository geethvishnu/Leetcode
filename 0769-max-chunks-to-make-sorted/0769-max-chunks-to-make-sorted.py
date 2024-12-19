class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = -1
        chunks = 0
        
        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])
            if max_so_far == i:
                chunks += 1
        
        return chunks
        