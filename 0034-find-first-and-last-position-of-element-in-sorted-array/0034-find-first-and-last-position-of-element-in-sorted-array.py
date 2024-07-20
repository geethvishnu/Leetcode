class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

    
        def binarySearchLeft(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    right = mid - 1
            return -1
        
        def binarySearchRight(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1
            return -1

        # Find the first and last position of the target
        left_index = binarySearchLeft(nums, target)
        right_index = binarySearchRight(nums, target)
        
        return [left_index, right_index]