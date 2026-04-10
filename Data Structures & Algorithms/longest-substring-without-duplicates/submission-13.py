class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        numset = set()

        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in numset:
                numset.remove(s[l])
                l+=1
            numset.add(s[i])
            res = max(res, i-l+1)
        return res








             


        