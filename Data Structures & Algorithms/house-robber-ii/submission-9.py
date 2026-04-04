class Solution:
    def rob(self, nums: List[int]) -> int:
        def houserobber(nums):
            robs1 = 0
            robs2 = 0

            for i in range(len(nums)):
                temp = max(nums[i]+robs1, robs2)
                robs1 = robs2
                robs2 = temp
            return robs2
        
        return max(nums[0], houserobber(nums[1:]), houserobber(nums[:-1]))