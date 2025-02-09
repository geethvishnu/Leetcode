class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if i<j and j-i!=nums[j]-nums[i]:
                    count+=1
        return count