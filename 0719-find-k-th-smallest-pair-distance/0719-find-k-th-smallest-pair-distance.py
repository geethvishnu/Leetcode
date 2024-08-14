class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dist=[]
        for i in range(n):
            for j in range(i+1,n):
                dist.append(abs(nums[i]-nums[j]))
        dist.sort()
        # print(dist)
        return dist[k-1]

        