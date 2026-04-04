class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, n in enumerate(nums):
            val = target - n
            if val in res:
                return [res[val], i]
            res[n] = i