class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        longest = 0
        l = 0

        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[i])
            longest = max(longest, (i-l+1))
        return longest
                

        








             


        