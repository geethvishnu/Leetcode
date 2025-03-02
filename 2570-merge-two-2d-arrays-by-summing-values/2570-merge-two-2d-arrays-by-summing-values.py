class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # result=[]
        # n1,n2=len(nums1),len(nums2)
        # if n1>n2:
        #     n=n2
        # else:
        #     n=n1
        # for i in range(n):
        #     for j in range(n):
        #         if nums1[i][0]==nums2[i][0]:
        #             result.append([nums1[i][0],nums1[i][1]+nums2[i][1]])
        #         else:
        #             result.append(nums1[i])
        #             result.append(nums2[i])
        # print(result)
        # result1 = list(map(list, set(map(tuple, result))))
        # print(result1)
        # return result1.sort()

        result={}
        for i, j in nums1:
            if i not in result:
                result[i]=j
        for i, j in nums2:
            if i in result:
                result[i]=result[i]+j
            else:
                result[i]=j
        # result1 = sorted(result.keys(), key=lambda x: x[0], reverse=True)
        result=sorted(result.items())
        # print(result1)
        return result