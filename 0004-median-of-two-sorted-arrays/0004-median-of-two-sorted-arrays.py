import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=[]

        # left,right=0,min(len(nums1),len(nums2))-1
        # while left<=right:
        #     if nums1[left]<nums2[right]:
        #         l.append(nums1[left])
                
        #         left+=1
        #     else:
        #         l.append(nums2[right])
        #         right-=1

        # m=len(nums1)+len(nums2)
        for i in nums1:
            l.append(i)
        for j in nums2:
            l.append(j)
        l.sort()
        m=len(l)-1
        # n=m/2
        # print(m,m//2)
        # print((l[(m//2)]+l[((m//2)+1)]))
        if m%2!=0:
            return (l[(m//2)]+l[((m//2)+1)])/2
        else:
            return l[(m)//2]
        # print(l)
            
        # return 2.00000
        