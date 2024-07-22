class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        substring=[]
        for i in range(n):
            for j in range(i+1,n+1):
                substring.append(s[i:j])
        m=0
        ls=''
        
        if len(substring)<2:
            return substring[0]
        if len(s)==2 and s[0]!=s[1]:
            return s[0]
        elif len(s)==2 and s[0]==s[1]:
            return s
        for i in substring:

            if len(i)<2:
                pass
            
            elif i[::-1]==i and m<len(i):
                m=len(i)
                ls=i
      

        return ls