class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left<0 or right>(2**31)-1:
            return 0
        result=0
        while left<right:
            left>>=1
            right>>=1
            result+=1
        return left<<result
    
            # sum=left
            # while left<=right:
            #     sum=sum&left
            #     left=left+1


            # return sum
        