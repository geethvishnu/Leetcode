class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hash table to store the frequency of each element
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Sort the hash table by frequency in descending order
        freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        
        # Select the k elements with the highest frequency
        result = []
        i = 0
        for num, count in freq.items():
            result.append(num)
            i += 1
            if i == k:
                break
        
        return result
