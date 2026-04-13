class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(list)

        for i, c in enumerate(s):
            freq[c].append(i)

        for val in freq.values():
            if len(val) == 1:
                return val[0]

        return -1  

        
        


        