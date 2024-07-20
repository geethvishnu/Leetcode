class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub = ""
        for char in s:
            if char.isalnum():  # Checking for alphanumeric characters
                sub += char
        sub = sub.lower()  # Convert to lowercase for case-insensitive comparison
        n = len(sub)
        m = n // 2
        if n % 2 == 0:
            return sub[:m] == sub[m:][::-1]  
        else:
            return sub[:m] == sub[m + 1:][::-1]  
            
