class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        if len(nums)==1:
            return nums[0]

        for i in range(0, len(nums)):
            if i == 0:
                if nums[i] != nums[i+1]:
                    return nums[i]
            elif i == (len(nums)-1):
                if nums[i]!=nums[i-1]:
                    return nums[i]
            else:
                if (nums[i-1]!=nums[i]) and (nums[i]!=nums[i+1]):
                    return nums[i]
            




        