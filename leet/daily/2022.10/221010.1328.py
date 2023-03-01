class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""

        for i in range(n//2):
            t = palindrome[i]
            if t=='a':
                continue
            else:
                return palindrome[:i] + 'a' + palindrome[i+1:]
        
        return palindrome[:-1] + 'b'