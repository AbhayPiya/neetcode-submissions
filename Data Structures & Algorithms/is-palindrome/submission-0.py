class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(c.lower() for c in s if c.isalnum()) # TC O(n) and SC O(n)
        if s== s[::-1]:
            return True
        return False
