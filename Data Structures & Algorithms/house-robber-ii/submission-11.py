class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxrob(arr):
            rob1 = rob2 = 0

            for i in arr:
                temp = max(rob2, i + rob1)
                rob1 = rob2
                rob2 = temp

            return rob2

        return max(nums[0], maxrob(nums[1:]), maxrob(nums[:-1]))
        