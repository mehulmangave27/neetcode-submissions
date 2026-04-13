class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        l = 0

        while l < len(intervals)-1:
            if intervals[l][1] >= intervals[l+1][0]:
                intervals[l][1] = max(intervals[l][1], intervals[l+1][1])
                intervals.pop(l+1)
            else:
                l+=1
        
        return intervals





      