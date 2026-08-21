class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}

        for i in s1:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        L=0
        R=len(s1)-1

        while R<len(s2):
            fresh = freq.copy()
            for i in range(L,R+1):
                

                if s2[i] in fresh:
                    fresh[s2[i]]-=1
                    if fresh[s2[i]]==0:
                        del fresh[s2[i]]
                
                if len(fresh)==0:
                    return True

            L+=1
            R+=1

        return False

