class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        initial_diff = nums[-1] - nums[0]
        
        min_diff = initial_diff
        
        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)
            min_diff = min(min_diff, high - low)
        
        return min_diff

        