class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = set()

        for n in nums:
            if n in res:
                return n
            else:
                res.add(n)
        
        