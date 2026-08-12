class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(c.lower() for c in s if c.isalnum()) # TC O(n) and SC O(n)
        if s== s[::-1]:
            return True
        return False

#same but other style:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]