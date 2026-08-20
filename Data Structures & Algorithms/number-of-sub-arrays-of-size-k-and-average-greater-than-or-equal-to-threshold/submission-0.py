class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target=k*threshold

        window_sum=sum(arr[:k])
        ans=0

        if window_sum>=target:
            ans+=1

        for R in range(k,len(arr)):
            window_sum+=arr[R]
            window_sum-=arr[R-k]
            if window_sum>=target:
                ans+=1
        
        return ans


        