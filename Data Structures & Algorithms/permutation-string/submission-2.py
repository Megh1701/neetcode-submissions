class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       
        freq={}

        for i in s1:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        L=0
        window={}

        for R in range(len(s2)):

            window[s2[R]]=window.get(s2[R],0)+1

            if R-L+1>len(s1):
                window[s2[L]]-=1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L+=1
            
            if freq==window:
                return True
            
        return False

