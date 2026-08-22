class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:  #eg: first ma act, second ma pot
            count=[0]* 26 ##asigning number for alphabets

            for ch in s: #eg: first ko act --> ch='a', ch='c', ch='t'
                count[ord(ch)-ord('a')]+=1 #ord() gives you the numerical Unicode value of a character. (so a-a=97-97= 0, c-a=99-97=2....) --> indext of s is assigning number a=0, b=1, c=2
            res[tuple(count)].append(s) ##why tuple(count) -->lists cannot be used as dictionary keys.

        return list(res.values())
                
''' "eat"
 ↓
count characters
 ↓
[a:1, e:1, t:1]
 ↓
use this count as dictionary key
 ↓
groups[key] = ["eat"]'''