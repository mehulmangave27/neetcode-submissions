class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        cur_sum = 0

        for weight in w:
            cur_sum += weight
            self.prefix.append(cur_sum)
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])
        l, r = 0, len(self.prefix)-1

        while l<r:
            mid = (l+r)//2
            if self.prefix[mid] < target:
                l = mid+1
            else:
                r = mid

        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()