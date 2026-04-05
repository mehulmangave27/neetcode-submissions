class Solution:
    def maxDifference(self, s: str) -> int:
        res = {}

        for char in s:
            res[char] = 1 + res.get(char, 0)
        
        max_odd = float('-inf')
        min_even = float('inf')

        for count in res.values():
            if count%2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)
            
        return max_odd - min_even