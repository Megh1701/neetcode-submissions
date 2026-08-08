from math import ceil
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        n=len(nums)
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for key,val in freq.items():
            if val > n//3:
                ans.append(key)

        return ans