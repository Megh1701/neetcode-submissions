class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        localmax=0
        
        for i in range(1,len(arr)):

            for j in range(i,len(arr)):
                if localmax<=arr[j]:
                    localmax=arr[j]
            
            arr[i-1]=localmax
            localmax=0
        
        arr[len(arr)-1]=-1
        
        return arr

            

