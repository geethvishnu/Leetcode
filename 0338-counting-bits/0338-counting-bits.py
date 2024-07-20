class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[]
        for i in range(n+1):
            c=0
            num = str(bin(i)[2:])
            c=num.count('1')
            a.append(c)
        return a


        