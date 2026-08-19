class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L=0
        minAns=float("inf")
        total=0
        for R in range(len(nums)):
            total+=nums[R]

            while total>=target:
                minAns=min(minAns,R-L+1)
                total-=nums[L]
                L+=1

        return 0 if minAns == float('inf') else minAns

