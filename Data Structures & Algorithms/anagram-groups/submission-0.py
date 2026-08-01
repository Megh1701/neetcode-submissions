class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)

        for i in strs:

            key=[0]*26

            for ch in i:

                key[ord(ch)-ord('a')]+=1

            key=tuple(key)

            freq[key].append(i)
        
        return list(freq.values())