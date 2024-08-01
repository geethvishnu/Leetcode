class Solution:
    def countSeniors(self, details: List[str]) -> int:
        aboveSixty=0
        sixty=0
        n=15  

        for i in details:
            aboveSixty=int(i[11:13])
            if aboveSixty>60:
                sixty+=1 
        return sixty
        