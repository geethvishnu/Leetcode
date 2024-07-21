class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=len(height)-1
        maxarea=0
        while left<=right:
            width=right-left
            diff=min(height[left],height[right])
            carea=width*diff
            if carea>maxarea:
                maxarea=carea
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxarea


        