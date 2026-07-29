class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        else:
            freqS={}
            freqT={}

            for ch in s:
                if ch in freqS:
                    freqS[ch]+=1
                else:
                    freqS[ch]=1
            
            for ch in t:
                if ch in freqT:
                    freqT[ch]+=1
                else:
                    freqT[ch]=1

        return freqT==freqS

