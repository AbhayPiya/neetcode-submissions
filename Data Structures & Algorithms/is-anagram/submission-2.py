class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return sorted(s) == sorted(t)  # TC: O(n logn), SC: O(n)
        count_s={}
        count_t={}
        
        for char in s:
            count_s[char]= count_s.get(char,0)+1
        
        for char in t:
            count_t[char]= count_t.get(char,0)+1
        
        return count_s == count_t
        


