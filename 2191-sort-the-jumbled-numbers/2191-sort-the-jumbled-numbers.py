from collections import Counter
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
            # l=[]
            # for i in nums:
            #     a=i 
            #     digit=0
                
            #     # place=1
            #     while a>0:
            #         rem=a%10
            #         digit=digit*10+mapping[rem]
            #         a//=10
            #     digit=str(digit)
            #     digit=int(digit[::-1])
            #     l.append(digit)
            # print(l)
            # d={}
            # for i in range(len(nums)):
            #     d[nums[i]]=l[i]
            # d1=dict(sorted(d.items(),key=lambda x:x[1]))
            # print(d1)
            # b=[]
            # for i,j in d1.items():
            #     b.append(i)
            # print(b)

            # if 0 in nums:
            #     b.pop(0)
            #     b.append(0)
            # # # count=Counter(l)
            # # # sortedlist=sorted(l,key=lambda x:(count[x],x))
            # # sortedlist=sorted(nums,key=lambda x:(d[x],x))
            # # print(sortedlist)
            # # n=len(nums)
            # # for i in range(n):
            # #     for j in range(0,n-i-1):
            # #         if l[j]>l[j+1]:
            # #             nums[j],nums[j+1]=nums[j+1],nums[j]


            # return b

            l=[]
            for i, n in enumerate(nums):
                n=str(n)
                digit=0
                for c in n:
                    digit=digit*10+mapping[int(c)]
                l.append((digit,i))
            l.sort()
            print(l)
            for i,j in l:
                print(i,j) 
            return [nums[j] for i,j in l]
        
            