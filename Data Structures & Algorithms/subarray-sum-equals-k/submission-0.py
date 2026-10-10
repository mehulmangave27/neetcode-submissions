class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        cursum = 0
        count = 0

        for n in nums:
            cursum += n
            value = cursum - k
            
            count+=prefix[value]
            
            prefix[cursum]+=1

        return count

        