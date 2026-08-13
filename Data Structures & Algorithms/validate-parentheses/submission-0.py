class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s: #brute force TC(O(n^2)) and SC (O(n))
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')

        return s==''

