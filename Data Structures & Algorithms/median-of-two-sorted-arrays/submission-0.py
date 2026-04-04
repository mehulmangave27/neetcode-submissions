class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        l,r = 0,0
        t = len(nums3)//2
        
        if len(nums3)%2==0:
            l,r = nums3[t-1],nums3[t]
            a = (l + r)/2
            return a
        else:
            return nums3[t]


        return
        