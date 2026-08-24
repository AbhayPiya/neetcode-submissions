class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset= set(nums)
        longest=0

        for n in nums:
            ##check if its the start of a sequence 
            if (n-1) not in numset: ##check starting left neighbor 
                length=0
                while (n+length) in numset:
                    length += 1
                    longest = max(length, longest)
        return longest