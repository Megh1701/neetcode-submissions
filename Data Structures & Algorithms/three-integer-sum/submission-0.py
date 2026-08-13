class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]

        for i in range(len(nums)):
            seen={}
            for j in range(i+1,len(nums)):
                nums_K=-(nums[i]+nums[j])

                if nums_K in seen:
                    Triplet=[nums[i],nums[j],nums_K]

                    if Triplet not in ans:
                        ans.append(Triplet)

                seen[nums[j]]=True
        
        return ans 