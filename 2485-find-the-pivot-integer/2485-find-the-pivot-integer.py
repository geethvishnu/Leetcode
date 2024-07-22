import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        xs=(n*(n+1))//2
        x = int(math.isqrt(xs))
        if x*x==xs:
            return x
            
        return -1
