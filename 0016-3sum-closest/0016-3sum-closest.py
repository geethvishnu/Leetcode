
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        maximum = 999999
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(maximum - target):
                    maximum = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return target
        
        return maximum