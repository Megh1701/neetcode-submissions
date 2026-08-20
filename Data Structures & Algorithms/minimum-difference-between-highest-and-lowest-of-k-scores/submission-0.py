class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minans=float('inf')
        L=0
        R=k-1

        while R<len(nums):
            total=nums[R]-nums[L]
            minans=min(minans,total)
            L+=1
            R+=1

        return int(minans)