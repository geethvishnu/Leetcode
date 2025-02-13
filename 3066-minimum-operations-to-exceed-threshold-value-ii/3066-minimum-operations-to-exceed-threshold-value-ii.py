import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert the array into a min-heap
        heapq.heapify(nums)
        operations = 0

        while len(nums) > 1:
            # Get the two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            # Check if the smallest number is already >= k
            if x >= k:
                return operations

            # Perform the operation
            new_value = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_value)
            operations += 1

        # Check if the last remaining element is >= k
        if nums[0] < k:
            return -1  # Impossible to make all elements >= k
        return operations
