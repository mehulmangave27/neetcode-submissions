class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        t = s[::-1]
        
        
        if s == t:
            return True
        else:
            return False

        