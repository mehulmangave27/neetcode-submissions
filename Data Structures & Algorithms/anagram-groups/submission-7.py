class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charmap = defaultdict(list)

        res = []

        for word in strs:
            count = [0]*26

            for c in word:
                count[ord(c) - ord('a')]+=1
            
            charmap[tuple(count)].append(word)

        return list(charmap.values())

        
        