class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #bucket= set()
        
        # for n in nums:
        #     if n in bucket:
        #         return True
        #     else:
        #         bucket.add(n)
            
        # return False
        sorted_num = sorted(nums) #O(nlogn)
        
        for i in range(len(sorted_num)-1):
            if sorted_num[i] ==sorted_num[i+1]:
                return True
        return False
