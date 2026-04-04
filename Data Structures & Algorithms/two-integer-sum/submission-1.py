class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       set = {}

       for i,j in enumerate(nums):
        diff = target - j
        if diff in set:
            return [set[diff],i]
        set[j] = i
       return
          