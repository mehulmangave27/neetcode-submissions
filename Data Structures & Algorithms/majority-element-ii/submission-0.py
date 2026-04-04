class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        n = len(nums)/3

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for j in count:
            if count[j]>n:
                res.append(j)
        return res

        