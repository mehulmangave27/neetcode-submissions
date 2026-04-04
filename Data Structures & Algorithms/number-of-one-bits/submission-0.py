class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        a = bin(n)
        string = str(a)
        for char in string:
            if char == '1':
                count+=1

        return count 
        