class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            

        for key,value in freq.items():
            if math.ceil(n/2) <= value:
                return key


