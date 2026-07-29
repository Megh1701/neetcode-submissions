class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        
        for i,n in enumerate(nums):
            diff=target-n
            if diff in freq:
                return [freq[diff],i]
            freq[n]=i
        return []