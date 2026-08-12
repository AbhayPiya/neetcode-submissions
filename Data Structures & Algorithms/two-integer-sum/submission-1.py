class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap= {}  #Hash map , TC (O(n)) and SC (O(n))
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n]=i
        return 

      