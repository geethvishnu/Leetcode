class Solution:
    def countOrders(self, n: int) -> int:
        if n==1:
            return 1
        choices=n*2
        fact=math.factorial(choices)//2**n
        return fact
        
        