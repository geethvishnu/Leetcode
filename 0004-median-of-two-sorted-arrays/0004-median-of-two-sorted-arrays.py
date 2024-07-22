import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # l=[]

        # left,right=0,min(len(nums1),len(nums2))-1
        # while left<=right:
        #     if nums1[left]<nums2[right]:
        #         l.append(nums1[left])
                
        #         left+=1
        #     else:
        #         l.append(nums2[right])
        #         right-=1

        # for i in nums1:
        #     l.append(i)
        # for j in nums2:
        #     l.append(j)
        # l.sort()
        # m=len(l)-1
        
        # if m%2!=0:
        #     return (l[(m//2)]+l[((m//2)+1)])/2
        # else:
        #     return l[(m)//2]

        merged = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        
        # Merging two sorted arrays
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Append remaining elements
        while i < m:
            merged.append(nums1[i])
            i += 1
        
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        # Finding the median
        total_len = m + n
        if total_len % 2 == 1:  # Odd length
            return merged[total_len // 2]
        else:  # Even length
            mid1, mid2 = total_len // 2 - 1, total_len // 2
            return (merged[mid1] + merged[mid2]) / 2.0
        
        