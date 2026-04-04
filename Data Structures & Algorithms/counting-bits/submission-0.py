class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(0,n+1):
            count = 0
            a = bin(i)
            string = str(a)
            for char in string:
                if char == '1':
                    count+=1
            arr.append(count)
        return arr

        