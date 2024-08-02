class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = sum(nums)
        
        if totalOnes == 0:
            return 0

        n = len(nums)
        currentOnes = sum(nums[:totalOnes])
        maxOnes = currentOnes

        for i in range(1, n):
            currentOnes = currentOnes - nums[i - 1] + nums[(i + totalOnes - 1) % n]
            maxOnes = max(maxOnes, currentOnes)

        return totalOnes - maxOnes



            