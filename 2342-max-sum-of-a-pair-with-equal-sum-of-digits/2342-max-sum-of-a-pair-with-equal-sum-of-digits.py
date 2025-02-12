class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        max_sum=-1
        for i in range(len(nums)):
            d_sum=sum(int(d) for d in str(nums[i]))
            if d_sum not in d:
                d[d_sum]=nums[i] 
            else:
                max_sum=max(max_sum, nums[i]+d[d_sum])
                d[d_sum]=max(d[d_sum], nums[i])

        return max_sum
