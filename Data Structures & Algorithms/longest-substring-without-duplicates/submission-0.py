class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0

        count = 0

        for i in range(0, len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l +=1

            charset.add(s[i])
            count = max(count, i-l+1)
        return count


        