from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort()
        d=Counter(nums)
        d1=sorted(nums, key=lambda x:(d[x],-x))
        

        return d1

        