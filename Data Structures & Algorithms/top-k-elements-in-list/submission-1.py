class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         ###Bucket sort : Complexity: O(n)
         count={}
         freq=[[]for i in range(len(nums)+1)]

         for n in nums:
            count[n]=1+count.get(n,0)
         for n,c in count.items():
            freq[c].append(n)
         res=[]
         for i in range(len(freq)-1,0,-1):  #going backwards because we want the most frequent numbers first --> range(start, stop, step) -1 is going backward
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
   
