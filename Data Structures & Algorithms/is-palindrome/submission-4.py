class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0, len(s)-1 ##Two pointer , TC (O(n)), SC (O(1))

        while l<r: ##the pointer hasn't meet same position if yes then palindrome
            while l<r and not s[l].isalnum(): #checking alphanumeric at position left
                l+=1
            while r>l and not s[r].isalnum(): #checking alphanumeric at right position
                r-=1
            
            if s[l].lower() != s[r].lower(): ##if left and right not same then false
                return False
            l,r= l+1,r-1
        return True   





