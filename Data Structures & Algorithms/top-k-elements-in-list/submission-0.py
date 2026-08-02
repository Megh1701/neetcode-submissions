class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        freq={}


        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        for key,val in freq.items():
            buckets[val].append(key)

        ans=[]

        for i in range(len(buckets)-1,0,-1):
            for nums in buckets[i]:
                ans.append(nums)

                if len(ans)==k:
                    break

            if len(ans)==k:
                break

        return ans