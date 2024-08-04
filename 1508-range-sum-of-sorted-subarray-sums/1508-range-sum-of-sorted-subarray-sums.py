class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarraysums=[]
        n=len(nums)
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                subarraysums.append(sum)
        print(subarraysums)
        newsum=0
        subarraysums.sort()
        while left<right+1:
            newsum+=subarraysums[left-1]
            left+=1
        print(newsum)

        return newsum

        