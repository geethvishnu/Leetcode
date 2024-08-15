class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0  # Number of $5 bills
        tens = 0   # Number of $10 bills
        
        for bill in bills:
            if bill == 5:
                fives += 1  # Take the $5 bill, no change needed
            elif bill == 10:
                if fives == 0:  # Need to give $5 as change but none available
                    return False
                fives -= 1  # Give back one $5 bill as change
                tens += 1  # Take the $10 bill
            else:  # bill == 20
                if tens > 0 and fives > 0:
                    tens -= 1  # Give back one $10 bill
                    fives -= 1  # Give back one $5 bill
                elif fives >= 3:
                    fives -= 3  # Give back three $5 bills
                else:
                    return False  # Cannot give the correct change
        
        return True 



            
            